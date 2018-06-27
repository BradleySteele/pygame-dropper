class Sprite:
    identifier = None
    rect = None

    def __init__(self, identifier, rect):
        self.identifier = identifier
        self.rect = rect


class TextSprite(Sprite):
    text = None

    def __init__(self, rect, text):
        super(TextSprite, self).__init__(text, rect)
        self.text = text

