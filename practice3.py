from abc import ABC, abstractmethod

class Libraryitem(ABC):

    def __init__(self, title, item_id):
        self._title = title
        self._item_id = item_id
        self.is_loaned = False

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def loan_period(self):
        pass

class Book(Libraryitem):
        def __init__(self, title, item_id, author, pages):
            super().__init__(title, item_id)
            self.author = author
            self.pages = pages

        def loan_period(self):
            return 14

        def info(self):
            return f"[도서] {self._title} / {self.author} / {self.pages}쪽"


b = Book("파이썬 입문", "B001", "박용웅", 480)
print(b.info())
print(b.loan_period())
print(b.is_loaned)

class DVD(Libraryitem):
       def __init__(self, title, item_id, director, minutes):
           super().__init__(title, item_id)
           self.director = director
           self.duration = minutes

       def loan_period(self):
           return 7

       def info(self):
           return f"[DVD] {self._title} / {self.director} 감독 / {self.duration}분"

class Magazine(Libraryitem):
       def __init__(self, title, item_id, issue):
              super().__init__(title, item_id)
              self.issue = issue

       def loan_period(self):
              return 3

       def info(self):
              return f"[잡지] {self._title} / {self.issue}호"


d = DVD("인터스텔라", "D001", "크리스토퍼 놀란", 169)
print(d.info())

m = Magazine("National Geographic", "M001", 123)
print(m.info())

from abc import ABC, abstractmethod

# ① 부모 클래스
class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_loaned = False
        self.borrower = None

    # 대출
    def checkout(self, name):
        if self.is_loaned:
            print(f"'{self.title}' 은(는) 이미 {self.borrower}님이 대출 중입니다.")
            return False

        self.is_loaned = True
        self.borrower = name

        print(f"{name}님, '{self.title}' 대출 완료! "
              f"(대출 기간 {self.loan_period()}일)")
        return True

    # 반납
    def return_item(self):
        if not self.is_loaned:
            print(f"'{self.title}' 은(는) 대출 중이 아닙니다.")
            return False

        print(f"{self.borrower}님이 '{self.title}'을(를) 반납했습니다.")

        self.is_loaned = False
        self.borrower = None

        return True

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def loan_period(self):
        pass


# ② Book
class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def loan_period(self):
        return 14

    def info(self):
        return f"[도서] {self.title} / {self.author} / {self.pages}쪽"


# ③ DVD
class DVD(LibraryItem):
    # ...
    pass


# ④ Magazine
class Magazine(LibraryItem):
    # ...
    pass


# ⑤ 객체 만들어서 테스트
b = Book("파이썬 입문", "B001", "박용웅", 480)

b.checkout("김민준")
b.checkout("이서연")
b.return_item()