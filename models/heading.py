
class Heading:
    
    def __init__(self, value, heading_size):
        self.value = value
        self.heading_size = heading_size

    def to_html(self):
        return f'<h{self.heading_size}>{self.value}</h{self.heading_size}>'

    def __str__(self):
        return self.to_html()

    def __repr__(self):
        return self.to_html()