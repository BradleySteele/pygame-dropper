class Sprite:
    rect = None

    def __init__(self, rect):
        self.rect = rect


class TextSprite(Sprite):
    text = None

    def __init__(self, rect, text):
        super(TextSprite, self).__init__(rect)
        self.text = text
