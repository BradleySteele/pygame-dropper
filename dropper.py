import pygame

import screen
import util


class Game:
    # Settings
    setting_width = 500
    setting_height = 500

    # Screens
    active_screen = None
    menu_screen = screen.MenuScreen(setting_width, setting_height)
    game_screen = screen.GameScreen(setting_width, setting_height)

    # Attributes
    running = False

    def __init__(self):
        self.active_screen = self.menu_screen


def start(game):
    game.running = True
    game.active_screen.show()

    handle_events(game)


def handle_events(game):
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                util.exit_program()
            elif event.type == pygame.MOUSEBUTTONUP:
                game.active_screen.clicked(game, pygame.mouse.get_pos())

        if game.active_screen.running:
            game.active_screen.show()
            pygame.display.update()


if __name__ == '__main__':
    start(Game())
