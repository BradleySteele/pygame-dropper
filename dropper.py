import pygame

import screen
import util


class Game:
    # Settings
    setting_width = 1000
    setting_height = 850

    # Screens
    active_screen = None
    menu_screen = screen.MenuScreen(setting_width, setting_height)
    game_screen = screen.GameScreen(setting_width, setting_height)
    end_game_screen = screen.EndGameScreen(setting_width, setting_height)

    # Attributes
    running = False
    score = 0
    high_score = 0
    iteration = 0
    difficulty = 10

    def __init__(self):
        self.active_screen = self.menu_screen


def start(game):
    """
    Initialises the provided game, should only be called once.

    :param game: the game to start.
    """

    game.running = True
    game.active_screen.show(game)

    handle_events(game)


def handle_events(game):
    """
    Handles all pygame events while the game is running.

    :param game: the game to handle events for.
    """

    while True:
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

        pygame.time.wait(game.difficulty)


if __name__ == '__main__':
    start(Game())
