from abc import abstractmethod
from random import randint

import pygame

import locale
import util
from sprite import TextSprite


class Screen:
    width = 0
    height = 0
    running = False

    surface = None
    sprites = []

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((width, height))

        pygame.display.set_caption(title)

    def show(self, game):
        if not self.running:
            self.running = True
            self.run(game)

    def hide(self):
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

    def __init__(self, width, height):
        super(MenuScreen, self).__init__(width, height, title='Dropper | Menu')

    def run(self, game):
        util.render_text(self, locale.MENU_TITLE, (200, 100), 50)
        util.render_text(self, locale.MENU_PLAY, (200, 200))
        util.render_text(self, locale.MENU_QUIT, (200, 250))

    def clicked(self, game, sprite):
        if type(sprite) == TextSprite:
            if sprite.text == locale.MENU_PLAY:
                game.active_screen.hide()
                game.active_screen = game.game_screen
                game.active_screen.show(game)
            elif sprite.text == locale.MENU_QUIT:
                util.exit_program()


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
        util.move_rect_from_id(self, locale.ID_PLAYER, (pygame.mouse.get_pos()[0], self.player_y), util.colour_black, util.colour_cyan)

        for sprite in self.sprites:
            if sprite.identifier == locale.ID_DROPPING_OBJECT:
                if sprite.part1.colliderect(self.sprite_player.rect) or sprite.part2.colliderect(self.sprite_player.rect):
                    game.active_screen.hide()
                    # TODO game over screen
                    game.active_screen = game.menu_screen
                    game.active_screen.show(game)
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
            game.iteration = 0
            gap = (100 - (game.score * 4))

            if gap < 5:
                gap = 5

            util.render_bar(self, locale.ID_DROPPING_OBJECT, util.colour_red, randint(0, (self.width - 100)), gap)

        pygame.draw.rect(self.surface, util.colour_cyan, self.sprite_score.rect)
        self.sprite_score = util.render_text(self, locale.GAME_SCORE.format(game.score), (70, 20), center=False)

    def run(self, game):
        game.score = 0
        game.iteration = 0

        self.surface.fill(util.colour_cyan)
        self.player_y = self.height - 70
        self.bar_hit_y = self.height - 75
        self.sprite_dirt = util.render_rect(self, locale.ID_DIRT, util.colour_brown, (0, (self.height - 35), self.width, 35))
        self.sprite_grass = util.render_rect(self, locale.ID_GRASS, util.colour_green, (0, (self.height - 45), self.width, 10))
        self.sprite_player = util.render_rect(self, locale.ID_PLAYER, util.colour_black, ((self.width / 2), self.player_y, 40, 25))
        self.sprite_score = util.render_text(self, locale.GAME_SCORE.format(game.score), (70, 20), center=False)

    def clicked(self, game, sprite):
        pass
