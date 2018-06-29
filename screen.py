from abc import abstractmethod
from random import randint

import pygame

import dropper_locale
import util
from sprite import TextSprite


class Screen:
    width = 0
    height = 0
    title = None
    running = False

    surface = None
    sprites = []

    def __init__(self, width, height, title):
        """
        :param width:  width of the screen.
        :param height: height of the screen.
        :param title:  title of the screen.
        """

        self.width = width
        self.height = height
        self.title = title
        self.surface = pygame.display.set_mode((width, height))

    def show(self, game):
        """
        Shows the screen and sets the caption.

        :param game: the game to show.
        """

        if not self.running:
            pygame.display.set_caption(self.title)
            self.running = True
            self.run(game)

    def hide(self):
        """
        Clears the active screen and its sprites.
        """

        self.running = False
        self.sprites = []
        self.surface.fill(util.colour_black)

    @abstractmethod
    def run(self, game):
        """
        Called when show() is invoked and the screen is not already
        running.
        """

        pass

    @abstractmethod
    def clicked(self, game, sprite):
        """
        Invoked when a pygame.MOUSEBUTTONUP event is handled with
        this as the active screen.

        :param game:     the game that the screen is bound to.
        :param sprite:   the position of the click provided by the event.
        """

        pass


class MenuScreen(Screen):
    """
    The menu screen provides access to all of the other screens and
    the ability to exit the program completely.
    """

    def __init__(self, width, height):
        super(MenuScreen, self).__init__(width, height, title='Dropper | Menu')

    def run(self, game):
        util.render_text(self, dropper_locale.MENU_TITLE, (200, 100), 50)
        util.render_text(self, dropper_locale.MENU_PLAY, (200, 200))
        util.render_text(self, dropper_locale.MENU_HOW_TO_PLAY, (200, 250))
        util.render_text(self, dropper_locale.MENU_QUIT, (200, 300))

    def clicked(self, game, sprite):
        if type(sprite) == TextSprite:
            if sprite.text == dropper_locale.MENU_PLAY:
                util.display_screen(game, game.game_screen)
            elif sprite.text == dropper_locale.MENU_HOW_TO_PLAY:
                util.display_screen(game, game.how_to_play_screen)
            elif sprite.text == dropper_locale.MENU_QUIT:
                util.exit_program()


class EndGameScreen(Screen):

    def __init__(self, width, height):
        super(EndGameScreen, self).__init__(width, height, title='Dropper | End Game')

    def show(self, game):
        if game.score > game.high_score:
            game.high_score = game.score

        super().show(game)

    def run(self, game):
        util.render_text(self, dropper_locale.END_GAME_TITLE, (200, 100), 50)
        util.render_text(self, dropper_locale.END_GAME_SCORE.format(game.score), (200, 200), 25)
        util.render_text(self, dropper_locale.END_GAME_HIGH_SCORE.format(game.high_score), (200, 230), 25)
        util.render_text(self, dropper_locale.END_GAME_PLAY_AGAIN, (200, 300))
        util.render_text(self, dropper_locale.END_GAME_RETURN_TO_MENU, (200, 350))

    def clicked(self, game, sprite):
        if sprite.identifier == dropper_locale.END_GAME_PLAY_AGAIN:
            util.display_screen(game, game.game_screen)
        elif sprite.identifier == dropper_locale.END_GAME_RETURN_TO_MENU:
            util.display_screen(game, game.menu_screen)


class HowToPlayScreen(Screen):

    def __init__(self, width, height):
        super(HowToPlayScreen, self).__init__(width, height, title='Dropper | How to Play')

    def run(self, game):
        util.render_text(self, dropper_locale.HOW_TO_PLAY_TITLE, (200, 100), 50)
        util.render_text(self, dropper_locale.HOW_TO_PLAY_LINE_1, (200, 200), 25)
        util.render_text(self, dropper_locale.HOW_TO_PLAY_LINE_2, (200, 225), 25)
        util.render_text(self, dropper_locale.HOW_TO_PLAY_LINE_3, (200, 250), 25)
        util.render_text(self, dropper_locale.HOW_TO_PLAY_GO_BACK, (200, 300), 25)

    def clicked(self, game, sprite):
        if sprite.identifier == dropper_locale.HOW_TO_PLAY_GO_BACK:
            util.display_screen(game, game.menu_screen)


class GameScreen(Screen):
    sprite_score = None
    sprite_dirt = None
    sprite_grass = None
    sprite_player = None

    player_y = 0
    bar_hit_y = 0

    def __init__(self, width, height):
        super(GameScreen, self).__init__(width, height, title='Dropper | Game')

    def show(self, game):
        super().show(game)
        util.move_rect_from_id(self, dropper_locale.ID_PLAYER, (pygame.mouse.get_pos()[0], self.player_y), util.colour_black, util.colour_cyan)

        for sprite in self.sprites:
            if sprite.identifier == dropper_locale.ID_DROPPING_OBJECT:
                if sprite.part1.colliderect(self.sprite_player.rect) or sprite.part2.colliderect(self.sprite_player.rect):
                    util.display_screen(game, game.end_game_screen)
                    return
                elif sprite.rect.y >= self.bar_hit_y:
                    self.sprites.remove(sprite)
                    pygame.draw.rect(self.surface, util.colour_cyan, sprite.part1)
                    pygame.draw.rect(self.surface, util.colour_cyan, sprite.part2)

                    game.score += 1
                else:
                    util.move_bar(self.surface, sprite, 2, util.colour_red, util.colour_cyan)

        game.iteration += 1

        if game.iteration >= 100:
            if game.score != 0 and game.score % 5 == 0 and game.difficulty > 3:
                game.difficulty -= 1

            game.iteration = 0
            gap = (100 - (game.score * 4))

            if gap < 5:
                gap = 5

            util.render_bar(self, dropper_locale.ID_DROPPING_OBJECT, util.colour_red, randint(0, (self.width - 100)), gap)

        pygame.draw.rect(self.surface, util.colour_cyan, self.sprite_score.rect)
        self.sprite_score = util.render_text(self, dropper_locale.GAME_SCORE.format(game.score), (70, 20), center=False)

    def run(self, game):
        game.score = 0
        game.iteration = 0
        game.difficulty = 10

        self.surface.fill(util.colour_cyan)
        self.player_y = self.height - 70
        self.bar_hit_y = self.height - 75
        self.sprite_dirt = util.render_rect(self, dropper_locale.ID_DIRT, util.colour_brown, (0, (self.height - 35), self.width, 35))
        self.sprite_grass = util.render_rect(self, dropper_locale.ID_GRASS, util.colour_green, (0, (self.height - 45), self.width, 10))
        self.sprite_player = util.render_rect(self, dropper_locale.ID_PLAYER, util.colour_black, ((self.width / 2), self.player_y, 40, 25))
        self.sprite_score = util.render_text(self, dropper_locale.GAME_SCORE.format(game.score), (70, 20), center=False)

    def clicked(self, game, sprite):
        pass
