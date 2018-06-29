import sys
import pygame

from sprite import TextSprite, Sprite, BarSprite

# Initialise all imported pygame modules
pygame.init()

colour_black = pygame.Color('black')
colour_white = pygame.Color('white')
colour_green = (14, 201, 39)
colour_brown = (99, 50, 4)
colour_cyan = (11, 216, 239)
colour_red = (178, 7, 7)


def render_text(screen, text, position, size=30, center=True):
    """
    Renders text and wraps in the TextSprite sprite, binding it
    to the provided screen with optional size and centering.

    :param screen:   screen that we're drawing on.
    :param text:     text to display.
    :param position: tuple of x and y position.
    :param size:     font size.
    :param center:   should the text be horizontally centered.
    :return: sprite wrapper for the string text.
    """

    font = pygame.font.Font('data/fonts/arial.ttf', size)
    render = font.render(text, True, colour_white, position)
    rect = render.get_rect(center=(screen.width / 2, position[1]) if center else position)

    screen.surface.blit(render, rect)
    return apply_sprite(screen, TextSprite(rect, text))


def render_rect(screen, identifier, colour, position):
    """
    Renders a rectangle and wraps into a Sprite, binding it
    to the provided screen.

    :param screen:     screen that we're drawing on.
    :param identifier: id for the sprite.
    :param colour:     colour of the rect.
    :param position:   position of the rect.
    :return: wrapped sprite for the rect.
    """

    rect = pygame.draw.rect(screen.surface, colour, position)
    return apply_sprite(screen, Sprite(identifier, rect))


def render_bar(screen, identifier, colour, length, gap):
    """
    Renders a bar and wraps into a BarSprite, binding it to
    the provided screen.

    :param screen:     screen that we're drawing on.
    :param identifier: id for the sprite.
    :param colour:     colour of the rect.
    :param length:     length of the first bar.
    :param gap:        size of the gap between both bars.
    :return: wrapped sprite for the bar.
    """

    part1 = pygame.draw.rect(screen.surface, colour, (0, 50, length, 25))
    part2 = pygame.draw.rect(screen.surface, colour, ((length + gap + 50), 50, ((screen.width - length) - gap), 25))
    return apply_sprite(screen, BarSprite(identifier, part1, part2))


def move_rect_from_id(screen, identifier, position, draw_colour, replace_colour):
    """
    Moves all sprites with the provided identifier and draws over
    the previous, if no sprites exist in the screen with the id,
    then the screen will not be affected.

    :param screen:         screen that we're drawing on.
    :param identifier:     id of the sprite to move.
    :param position:       new position of the sprite.
    :param draw_colour:    colour of the rect.
    :param replace_colour: colour to replace previous position.
    """

    for sprite in screen.sprites:
        if sprite.identifier == identifier:
            move_rect(screen.surface, sprite.rect, position, draw_colour, replace_colour)


def move_rect(surface, rect, position, draw_colour, replace_colour):
    """
    Moves a rectangle and draws over the previous.

    :param surface:        surface that we're drawing on.
    :param rect:           rect to move.
    :param position:       new position of the sprite.
    :param draw_colour:    colour of the rect.
    :param replace_colour: colour to replace previous position.
    """

    pygame.draw.rect(surface, replace_colour, rect)
    rect.x = position[0]
    rect.y = position[1]
    pygame.draw.rect(surface, draw_colour, rect)


def move_bar(surface, sprite, y, draw_colour, replace_colour):
    """
    Moves a bar and draws over the previous.

    :param surface:        surface that we're drawing on.
    :param sprite:         sprite to move.
    :param y:              y axis to move, relative.
    :param draw_colour:    colour of the rect.
    :param replace_colour: colour to replace previous position.
    """

    move_rect(surface, sprite.part1, (sprite.part1.x, sprite.part1.y + y), draw_colour, replace_colour)
    move_rect(surface, sprite.part2, (sprite.part2.x, sprite.part2.y + y), draw_colour, replace_colour)


def apply_sprite(screen, sprite):
    """
    Applies a sprite to the provided screen.

    :param screen: screen to apply the sprite to.
    :param sprite: sprite to apply.
    :return: the applied sprite.
    """

    screen.sprites.append(sprite)
    return sprite


def display_screen(game, screen):
    """
    Hides the active screen and sets and shows the provided
    screen as the new for the game.

    :param game:   the game to display the screen for.
    :param screen: the screen to display.
    """

    game.active_screen.hide()
    game.active_screen = screen
    game.active_screen.show(game)


def exit_program():
    """
    Quits pygame and exists the program.
    """

    print("Stopping dropper game. Good bye!")

    pygame.quit()
    sys.exit()
