from book import Book
from member import Member
from transaction import Transaction
from datetime import date 
import time

class Library:

    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []


    def loadData(self):
        self.loadBooks()
        self.loadMembers()
        self.loadTransactions()

    def loadBooks(self):
        with open(r"data\books.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                book = Book(int(data[0]), data[1].strip(), data[2].strip(), data[3].strip(), int(data[4]), data[5].strip().lower()=="true")
                self.books.append(book)


    def loadMembers(self):
        with open(r"data\members.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        if data[2]:
                             borrowedBooks = [int(x) for x in data[2].split(";")]
                        else:
                             borrowedBooks = []
                        member = Member(int(data[0]), data[1].strip(), borrowedBooks)
                        self.members.append(member)

    def loadTransactions(self):
        with open(r"data\transactions.txt", "r") as file:
                    for line in file:
                        data = line.strip().split(",")
                        transaction = Transaction(int(data[0]), int(data[1]), int(data[2]), date.fromisoformat(data[3].strip()), data[4].strip())
                        self.transactions.append(transaction)

    def manageBooks(self):
        while True:
            choice = input("\n\nPlease select an option: \n" \
            "1. Add book \n" \
            "2. Remove book \n" \
            "3. Edit book \n" \
            "4. Display books \n" \
            "5. Search for a book \n" \
            "6. View available books \n" \
            "7. View borrowed books \n" \
            "8. Back \n")

            try:
                choice = int(choice)
                if choice < 1 or choice > 8:
                    print("Please enter a number between 1 and 8.\n")
                    continue
            except ValueError:
                 print("Invalid input. Please enter a number.\n")
                 continue

            if choice == 1:
                 self.addBook()

            elif choice == 2:
                 self.removeBook()

            elif choice == 3:
                 self.editBook()

            elif choice == 4:
                 self.displayBooks()

            elif choice == 5:
                 self.searchBooks()

            elif choice == 6:
                 self.viewAv()

            elif choice == 7:
                 self.viewBo()

            elif choice == 8:
                 break

    def addBook(self):
         if self.books:
            newid = max(book.bookid for book in self.books) + 1
         else:
            newid = 0

         while True:
              newtitle = input("\n\nPlease enter the title: ")
              newauthor = input("Please enter the author: ")
              newcategory = input("Please enter the category: ")
              newpublication = input("Please enter the publication year: ")
              newavailability = input("Please enter the availability (true/false): ")

              try:
                   newpublication = int(newpublication)
                   if newavailability.lower() not in ("true", "false"):
                        print("Please enter a valid availability.")
                        continue
                   newavailability = newavailability.lower() == "true"

              except ValueError:
                   print("Please enter a valid publication year.")
                   continue

              book = Book(newid, newtitle, newauthor, newcategory, newpublication, newavailability)
              self.books.append(book)
              print("Book added successfully!")
              break

    def removeBook(self):
         while True:
            removeid = input("\n\nPlease enter the ID of the book you would like to remove: ")
            try:
                 removeid = int(removeid)
                 book = self.searchbyid(removeid)
                 if book == []:
                      print("ID does not exist, please enter a valid ID.")
                      continue
            except ValueError:
                 print("Please enter a valid ID number.")
                 continue
            break
         self.books.remove(book)
         print("Book removed sucessfully!")

    def editBook(self):
        while True:
             editid = input("Please enter the ID of the book you would like to edit: ")
             try:
                  editid = int(editid)
                  book = self.searchbyid(editid)
                  if book is None:
                       print("ID does not exist, please enter a valid ID")
                       continue
             except ValueError:
                  print("Enter a valid ID number.")
                  continue
             break

        while True:
          edittitle = input("\n\nPlease enter the title: ")
          editauthor = input("Please enter the author: ")
          editcategory = input("Please enter the category: ")
          editpublication = input("Please enter the publication year: ")
          editavailability = input("Please enter the availability (true/false): ")
        
          try:
               editpublication = int(editpublication)
               if editavailability.lower() not in ("true", "false"):
                    print("Please enter a valid availability.")
                    continue
               editavailability = editavailability.lower() == "true"
        
          except ValueError:
               print("Please enter a valid publication year.")
               continue

          book.update_details(edittitle, editauthor, editcategory, editpublication, editavailability)
          print("Book updated successfully!")
          break

        

    def displayBooks(self):
         if not self.books:
              print("No books in the library")
              return
         
         for book in self.books:
              print(book.display_info())

         

    def searchBooks(self):
         while True:
               choice = input("\n\nPlease select an option: \n" \
                    "1. Search by ID \n" \
                    "2. Search by Title \n" \
                    "3. Search by Author \n" \
                    "4. Search by Category \n" \
                    "5. Search by Publication Year \n" \
                    "6. Back \n")
         
               try:
                    choice = int(choice)
                    if choice < 1 or choice > 7:
                         print("Please enter a number between 1 and 6.\n")
                         continue
               except ValueError:
                    print("Invalid input. Please enter a number.\n")
                    continue

               if choice == 1:
                    while True:
                         searchid = input("Please enter the ID you would like to search for: ")
                         try:
                              searchid = int(searchid)
                              if searchid < 0:
                                   print("Please enter a positive number.")
                                   continue
                         except ValueError:
                              print("Please enter a number.")
                              continue

                         book = self.searchbyid(searchid)
                         print(book.display_info())
                         break


               if choice == 2:
                    searchtitle = input("Please enter the title you would like to search for: ")
                    for book in self.searchbytitle(searchtitle):
                         print(book.display_info())
                    break

               if choice == 3:
                    searchauthor = input("Please enter the author you would like to search for: ")
                    for book in self.searchbyauthor(searchauthor):
                         print(book.display_info())

               if choice == 4:
                    searchcategory = input("Please enter the author you would like to search for: ")
                    for book in self.searchbycategory(searchcategory):
                         print(book.display_info())

               if choice == 5:
                    while True:
                         searchpub = input("Please enter the publication year you would like to search for:")

                         try:
                              searchpub = int(searchpub)
                         except ValueError:
                              print("Enter a valid year.")
                              continue
                         for book in self.searchbypub(searchpub):
                              print(book.display_info())
                         break

               if choice == 6:
                    break


    def viewAv(self):
         for book in self.books:
              if book.availability:
                   print(book.display_info())

    def viewBo(self):
          for book in self.books:
              if not book.availability:
                   print(book.display_info())

    def searchbyid(self, bookid):
         for book in self.books:
              if book.bookid == bookid:
                   return book

    def searchbytitle(self, title):
         res = []
         for book in self.books:
              if book.title.lower() == title.lower():
                   res.append(book)
         return res

    def searchbyauthor(self, author):
         res = []
         for book in self.books:
              if book.author.lower() == author.lower():
                   res.append(book)
         return res

    def searchbycategory(self, category):
         res = []
         for book in self.books:
              if book.category.lower() == category.lower():
                   res.append(book)
         return res    
    
    def searchbypub(self, publication):
         res = []
         for book in self.books:
              if book.publication == publication:
                   res.append(book)
         return res


    def manageMembers(self):
         while True:
               choice = input("\nPlease select an option: \n" \
               "1. Add member \n" \
               "2. Remove member \n" \
               "3. Search member \n" \
               "4. Display members \n" \
               "5. Back \n")
         
               try:
                    choice = int(choice)
                    if choice < 1 or choice > 5:
                         print("Please enter a number between 1 and 5.\n")
                         continue
               except ValueError:
                    print("Invalid input. Please enter a number.\n")
                    continue

               if choice == 1:
                    self.addMember()

               if choice == 2:
                    self.removeMember()

               if choice == 3:
                    self.searchMember()

               if choice == 4:
                    self.displayMembers()          

               if choice == 5:
                    break



    def addMember(self):
         if self.members:
            newid = max(member.memberid for member in self.members) + 1
         else:
            newid = 0
         newname = input("\n\nPlease enter the title: ")
         member = Member(newid, newname)
         self.members.append(member)
         print("Member added successfully!")

    def removeMember(self):
         while True:
            removeid = input("Please enter the ID of the member you would like to remove: ")
            try:
                 removeid = int(removeid)
                 member = self.searchbymid(removeid)
                 if member is None:
                      print("ID does not exist, please enter a valid ID.")
                      continue
            except ValueError:
                 print("Please enter a valid ID number.")
                 continue
            break
         self.members.remove(member)
         print("Member removed sucessfully!")


    def searchMember(self):
         while True:
               choice = input("\n\nPlease select an option: \n" \
                    "1. Search by ID \n" \
                    "2. Search by Name \n" \
                    "3. Back \n" \
                    )
         
               try:
                    choice = int(choice)
                    if choice < 1 or choice > 3:
                         print("Please enter a number between 1 and 3.\n")
                         continue
               except ValueError:
                    print("Invalid input. Please enter a number.\n")
                    continue

               if choice == 1:
                         searchid = input("Please enter the ID you would like to search for: ")
                         try:
                              searchid = int(searchid)
                              if searchid < 0:
                                   print("Please enter a positive number.")
                                   continue
                         except ValueError:
                              print("Please enter a number.")
                              continue

                         member = self.searchbymid(searchid)
                         print(member.display_info())
                         break

               if choice == 2:
                    searchname = input("Please enter the name you would like to search for: ")
                    for member in self.searchbyname(searchname):
                         print(member.display_info())
                    break

               if choice == 3:
                    break



    def displayMembers(self):
         if not self.members:
              print("No members in the registry")
              return
         
         for member in self.members:
              print(member.display_info())


    def searchbymid(self, memberid):
         for member in self.members:
              if member.memberid == memberid:
                   return member

    def searchbyname(self, name):
         res = []
         for member in self.members:
              if member.name.lower() == name.lower():
                   res.append(member)
         return res



    def borrowBook(self):
          while True:
               memberid = input("\n\nPlease enter your member ID: ")
               try:
                    memberid = int(memberid)
                    if memberid < 0:
                         print("Please enter a positive number.")
                         continue
               except ValueError:
                    print("Please enter a number.")
                    continue
               member = self.searchbymid(memberid)
               if member is None:
                    print("Please enter a valid ID.")
                    continue
               else:
                    break

          while True:
               bookid = input("Please enter the book ID: ")
               try:
                    bookid = int(bookid)
                    if bookid < 0:
                         print("Please enter a positive number.")
                         continue
               except ValueError:
                    print("Please enter a number.")
                    continue
               book = self.searchbyid(bookid)
               if book is None:
                    print("Please enter a valid ID.")
                    continue
               else:
                    break
          if book.availability:
               member.borrowBook(bookid)
               book.update_details(None, None, None, None, False)
               if self.members:
                    transactionid = max(transaction.transactionid for transaction in self.transactions) + 1
               else:
                    transactionid = 0
               transaction = Transaction(transactionid, memberid, bookid, date.today(), "borrow")
               self.transactions.append(transaction)
               print("Book borrowed successfully!")
          else:
               print("Book not available.")


    def returnBook(self):
          while True:
               memberid = input("\n\nPlease enter your member ID: ")
               try:
                    memberid = int(memberid)
                    if memberid < 0:
                         print("Please enter a positive number.")
                         continue
               except ValueError:
                    print("Please enter a number.")
                    continue
               member = self.searchbymid(memberid)
               if member is None:
                    print("Please enter a valid ID.")
                    continue
               else:
                    break

          while True:
               bookid = input("Please enter the book ID: ")
               try:
                    bookid = int(bookid)
                    if bookid < 0:
                         print("Please enter a positive number.")
                         continue
               except ValueError:
                    print("Please enter a number.")
                    continue
               book = self.searchbyid(bookid)
               if book is None:
                    print("Please enter a valid ID.")
                    continue
               else:
                    break

          if bookid in member.borrowedBooks:
               member.returnBook(bookid)
               book.update_details(None, None, None, None, True)
               if self.members:
                    transactionid = max(transaction.transactionid for transaction in self.transactions) + 1
               else:
                    transactionid = 0
               transaction = Transaction(transactionid, memberid, bookid, date.today(), "return")
               self.transactions.append(transaction)
               print("Book returned successfully!")
          else:
               print("You do not have this book.")

    def viewTransactions(self):
         if not self.transactions:
              print("No transactions in database.")
              return
         
         for transaction in self.transactions:
              print(transaction.display_info())

    def saveData(self):
         with open(r"data\books.txt", "w") as file:
              for book in self.books:
                   file.write(f"{book.display_info()}\n")

         with open(r"data\members.txt", "w") as file:
              for member in self.members:
                   file.write(f"{member.display_info()}\n")

         with open(r"data\transactions.txt", "w") as file:
              for transaction in self.transactions:
                   file.write(f"{transaction.display_info()}\n")
