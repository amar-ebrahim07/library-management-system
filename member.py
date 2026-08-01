from datetime import date
from transaction import Transaction
from book import Book
from person import Person

class Member(Person):
    def __init__(self, memberid, name, borrowedBooks):
        super().__init__(memberid, name)
        self.borrowedBooks = borrowedBooks


    def display_info(self):
        borrowed = ";".join(str(bookid) for bookid in self.borrowedBooks)
        return (f"{self.memberid}, {self.name}, {borrowed}")


    def borrowBook(self, bookid):
        self.borrowedBooks.append(bookid)

    def returnBook(self,bookid):
        self.borrowedBooks.remove(bookid)

    def __str__(self):
        return(self.name)
