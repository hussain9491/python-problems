
class Book:
    def __init__(self, title, author, published, pages, available):
        self.title = title
        self.author = author
        self.published = published
        self.pages = pages
        self.available = available
    

    def read(self):
        print(f"yes, you can read {self.title} book")