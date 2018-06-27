class Sprite:
    identifier = None
    rect = None

    def __init__(self, identifier, rect):
        self.identifier = identifier
        self.rect = rect


class BarSprite(Sprite):
    part1 = None
    part2 = None

    def __init__(self, identifier, part1, part2):
        super(BarSprite, self).__init__(identifier, part1)
        self.part1 = part1
        self.part2 = part2


class TextSprite(Sprite):
    text = None

    def __init__(self, rect, text):
        super(TextSprite, self).__init__(text, rect)
        self.text = text

