from abc import abstractmethod

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

    def show(self):
        if not self.running:
            self.running = True
            self.run()

    def hide(self):
        self.running = False
        self.sprites = []
        self.surface.fill(util.colour_black)

    @abstractmethod
    def run(self):
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

    def run(self):
        util.render_text(self, locale.MENU_TITLE, (200, 100), 50)
        util.render_text(self, locale.MENU_PLAY, (200, 200))
        util.render_text(self, locale.MENU_QUIT, (200, 250))

    def clicked(self, game, sprite):
        if type(sprite) == TextSprite:
            if sprite.text == locale.MENU_PLAY:
                game.active_screen.hide()
                game.active_screen = game.game_screen
                game.active_screen.show()
            elif sprite.text == locale.MENU_QUIT:
                util.exit_program()


class GameScreen(Screen):

    def __init__(self, width, height):
        super(GameScreen, self).__init__(width, height, title='Dropper | Game')

    def show(self):
        super().show()
        util.move_rect(self, "player", (pygame.mouse.get_pos()[0], 442), util.colour_black, util.colour_cyan)

    def run(self):
        self.surface.fill(util.colour_cyan)
        util.render_rect(self, "dirt", util.colour_brown, (0, 465, 500, 35))
        util.render_rect(self, "grass", util.colour_green, (0, 455, 500, 10))
        util.render_rect(self, "player", util.colour_black, (230, 430, 40, 25))

    def clicked(self, game, sprite):
        print("Clicked: " + sprite.identifier)
