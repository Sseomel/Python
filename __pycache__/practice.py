class LibraryItem:
    def __init__(self, title):
        self.title = title


class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title)
        self.author = author
        self.pages = pages

    def loan_author(self):
        return self.author 

    

book = Book("파이썬 공부", 1, "홍길동", 300)

print(book.title)
print(book.author)
print(book.pages)
print(book.loan_author())