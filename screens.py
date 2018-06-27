import pygame

import util


class Screen:
    width = 0
    height = 0
    surface = None
    running = False

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((width, height))

        pygame.display.set_caption(title)

    def show(self):
        self.running = True

    def hide(self):
        self.running = False
        self.surface.fill(util.colour_white)

    def run(self):
        pass

    def clicked(self, game, position):
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
        print("Clicked[x=" + str(position[0]) + ",y=" + str(position[1]) + "]")
        game.active_screen.hide()
        game.active_screen = game.game_screen
        game.active_screen.show()


class GameScreen(Screen):

    def __init__(self, width, height):
        super(GameScreen, self).__init__(width, height, title='Dropper | Game')
