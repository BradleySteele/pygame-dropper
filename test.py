import sys
import pygame

import screens


class Game:
    # Settings
    setting_width = 500
    setting_height = 500

    # Screens
    active_screen = None
    menu_screen = screens.MenuScreen(setting_width, setting_height)
    game_screen = screens.GameScreen(setting_width, setting_height)

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
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                game.active_screen.clicked(game, pygame.mouse.get_pos())

        if game.active_screen.running:
            game.active_screen.run()
            pygame.display.update()


if __name__ == '__main__':
    start(Game())
