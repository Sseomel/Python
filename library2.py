from library import LibraryItem

class Book(LibraryItem):
def __init__(self, title, item_id, author, pages):
    super().__init__(title, item_id)
self.author = author
self.pages = pages 

def loan_period(self):
    return 14

def info(self):
    return f"[도서] {self.title} / {self.author} / {self.pages}"
