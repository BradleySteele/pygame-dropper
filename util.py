import pygame

# Initialise all imported pygame modules
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
    """

    font = pygame.font.Font('data/fonts/arial.ttf', size)
    text = font.render(text, True, colour_white, position)
    text_rect = text.get_rect(center=(screen.width / 2, position[1]) if center else position)

    screen.surface.blit(text, text_rect)
