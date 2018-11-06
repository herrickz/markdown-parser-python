
class InlineText:

    def __init__(self, value):
        self.value = value

    def to_html(self):
        return self.value

    def __str__(self):
        return self.to_html()

    def __repr__(self):
        return self.to_html()