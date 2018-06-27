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
    score = 0
    iteration = 0

    def __init__(self):
        self.active_screen = self.menu_screen


def start(game):
    game.running = True
    game.active_screen.show(game)

    handle_events(game)


def handle_events(game):
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                util.exit_program()
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for sprite in game.active_screen.sprites:
                    if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                        game.active_screen.clicked(game, sprite)

        if game.active_screen.running:
            game.active_screen.show(game)
            pygame.display.update()

        pygame.time.wait(10)


if __name__ == '__main__':
    start(Game())
