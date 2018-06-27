import sys
import pygame

# Initialise all imported pygame modules
from sprite import TextSprite, Sprite

pygame.init()

clock = pygame.time.Clock()

colour_black = pygame.Color('black')
colour_white = pygame.Color('white')
colour_green = (14, 201, 39)
colour_brown = (99, 50, 4)
colour_cyan = (11, 216, 239)


def render_text(screen, text, position, size=30, center=True):
    """
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
    rect = pygame.draw.rect(screen.surface, colour, position)
    return apply_sprite(screen, Sprite(identifier, rect))


def move_rect(screen, identifier, position, draw_colour, replace_colour):
    for sprite in screen.sprites:
        if sprite.identifier == identifier:
            pygame.draw.rect(screen.surface, replace_colour, sprite.rect)
            sprite.rect.center = position
            pygame.draw.rect(screen.surface, draw_colour, sprite.rect)


def apply_sprite(screen, sprite):
    """
    Applies a sprite to the provided screen.

    :param screen: screen to apply the sprite to.
    :param sprite: sprite to apply.
    :return: the applied sprite.
    """

    screen.sprites.append(sprite)
    return sprite


def exit_program():
    """
    Quits pygame and exists the program.
    """

    print("Stopping dropper game. Good bye!")

    pygame.quit()
    sys.exit()
