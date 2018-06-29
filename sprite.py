class Sprite:
    """
    The Sprite class is wrapper class for mapping an id with
    the rect.
    """

    identifier = None
    rect = None

    def __init__(self, identifier, rect):
        self.identifier = identifier
        self.rect = rect


class BarSprite(Sprite):
    """
    The BarSprite is a subclass of Sprite and provides two rects
    for one bar. The gap in a bar is literal, rather than having
    one rect and drawing a gap in it.
    """

    part1 = None
    part2 = None

    def __init__(self, identifier, part1, part2):
        super(BarSprite, self).__init__(identifier, part1)
        self.part1 = part1
        self.part2 = part2


class TextSprite(Sprite):
    """
    The TextSprite is used as a button-like sprite and by default
    uses the text as its identifier.
    """

    text = None

    def __init__(self, rect, text):
        super(TextSprite, self).__init__(text, rect)
        self.text = text

