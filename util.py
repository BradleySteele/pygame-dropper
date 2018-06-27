import sys
import pygame

# Initialise all imported pygame modules
from sprite import TextSprite

pygame.init()

clock = pygame.time.Clock()

colour_black = pygame.Color('black')
colour_white = pygame.Color('white')


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
    render_rect = render.get_rect(center=(screen.width / 2, position[1]) if center else position)

    screen.surface.blit(render, render_rect)
    return apply_sprite(screen, TextSprite(render_rect, text))


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
