from abc import abstractmethod

import pygame

import dropper
import util
from sprite import TextSprite


class Screen:
    width = 0
    height = 0
    surface = None
    running = False
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
        self.surface.fill(util.colour_white)

    def run(self):
        """
        Called when show() is invoked and the screen is not already
        running.
        """

        pass

    def clicked(self, game, position):
        """
        Invoked when a pygame.MOUSEBUTTONUP event is handled with
        this as the active screen.

        :param game:     the game that the screen is bound to.
        :param position: the position of the click provided by the event.
        """

        pass


class MenuScreen(Screen):

    def __init__(self, width, height):
        super(MenuScreen, self).__init__(width, height, title='Dropper | Menu')

    def run(self):
        self.surface.fill(util.colour_black)
        util.render_text(self, "Dropper", (200, 100), 50)
        util.render_text(self, "Play", (200, 200))
        util.render_text(self, "Quit", (200, 250))

        # pygame.draw.rect(self.surface, (255, 0, 0), (0, 0, 50, 30))

    def clicked(self, game, position):
        for sprite in self.sprites:
            if sprite.collidepoint(position):
                if type(sprite) == TextSprite:
                    if sprite.text == 'Play':
                        game.active_screen.hide()
                        game.active_screen = game.game_screen
                        game.active_screen.show()
                    elif sprite.text == 'Quit':
                        dropper.stop()


class GameScreen(Screen):

    def __init__(self, width, height):
        super(GameScreen, self).__init__(width, height, title='Dropper | Game')
