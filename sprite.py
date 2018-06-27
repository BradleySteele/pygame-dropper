class Sprite:
    rect = None

    def __init__(self, rect):
        self.rect = rect


class TextSprite:
    text = None

    def __init__(self, rect, text):
        super(TextSprite, self).__init__(self, rect)
        self.text = text
