from abc import ABC, abstractmethod


class Libraryitem(ABC):
    total_items = 0
    
    def __init__(self, title, item_id):
        self._title = title
        self._item_id = item_id
        self.is_loaned = False
        self._borrower = None

        Libraryitem.total_items += 1
        
    @abstractmethod
    def loan_period(self):
         pass
    
    @abstractmethod
    def info(self): 
        pass

    