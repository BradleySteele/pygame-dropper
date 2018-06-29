import unittest

import dropper_locale
import util
from dropper import Game


def get_sprite(screen, identifier):
    """
    Attempts to get the sprite with an identifier from the provided
    screen.

    :param screen:     the screen containing the sprite.
    :param identifier: id of the sprite.
    :return: the first sprite matching the given id, otherwise None.
    """

    for sprite in screen.sprites:
        if sprite.identifier == identifier:
            return sprite

    return None


class TestGameObject(unittest.TestCase):

    def test_first_screen_is_menu(self):
        """
        Checks that the first screen is the menu screen.
        """

        game = Game()
        self.assertEqual(game.active_screen, game.menu_screen)

    def test_game_ends_on_collision_with_bar(self):
        """
        Checks to see if the end game screen is displayed when a bar
        hits a player.
        """

        game = Game()
        util.display_screen(game, game.game_screen)

        # Fill screen with bar
        util.render_bar(game.active_screen, dropper_locale.ID_DROPPING_OBJECT, util.colour_red, game.setting_width, 0)

        # Move bar on top of player
        util.move_rect_from_id(game.active_screen, dropper_locale.ID_DROPPING_OBJECT, (0, game.game_screen.player_y),
                               util.colour_cyan, util.colour_black)

        # Run as if the game is ticking
        game.active_screen.show(game)

        self.assertEqual(game.active_screen, game.end_game_screen)

    def test_high_score_updated_on_end_shown(self):
        """
        Checks that the high score is updated when the end game screen
        is displayed.
        """

        game = Game()
        game.score = 10
        util.display_screen(game, game.end_game_screen)
        self.assertEqual(game.high_score, 10)

    def test_play_click_opens_game_screen(self):
        """
        Checks that the game screen is opened when the 'Play' text is
        clicked on the menu screen.
        """

        game = Game()

        # Load sprites by display the screen
        util.display_screen(game, game.menu_screen)

        # Fake a click event
        game.active_screen.clicked(game, get_sprite(game.menu_screen, dropper_locale.MENU_PLAY))
        self.assertEqual(game.active_screen, game.game_screen)

    def test_how_to_play_click_opens_how_to_play_screen(self):
        """
        Checks that the how to play screen is opened when the 'How
        to Play' text is clicked on the menu screen.
        """

        game = Game()
        util.display_screen(game, game.menu_screen)
        game.active_screen.clicked(game, get_sprite(game.menu_screen, dropper_locale.MENU_HOW_TO_PLAY))
        self.assertEqual(game.active_screen, game.how_to_play_screen)


if __name__ == '__main__':
    unittest.main()
