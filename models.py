class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def serialize(self):
        return {
            'title': self.title,
            'author': self.author
        }