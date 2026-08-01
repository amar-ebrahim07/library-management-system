from member import Member
from book import Book
from library import Library
import time

# check update books for errors
# rewrite members class and library 


# add a savedata function in library


def main():
    library = Library()
    library.loadData()

    while True:
     time.sleep(1)
     choice = input("\n\n\
        ==============================\n\
        University Library System\n\
         ==============================\n\
          1. Book Management\n\
          2. Member Management\n\
          3. Borrow Book\n\
          4. Return Book\n\
          5. View Transactions\n\
          6. Save Data\n\
          7. Exit\n\n\
          Enter your choice:")


     try:
        choice = int(choice)
        if choice < 1 or choice > 7:
            print("Please enter a number between 1 and 7.\n")
            continue

     except ValueError:
        print("Invalid input. Please enter a number.\n")
        continue


     if choice == 1:
        library.manageBooks()

     elif choice == 2:
        library.manageMembers()

     elif choice == 3:
        library.borrowBook()

     elif choice == 4:
        library.returnBook()
     
     elif choice == 5:
        library.viewTransactions()
     
     elif choice == 6:
        library.saveData()

     elif choice == 7:
        library.saveData()
        time.sleep(1)
        print("Exiting System...")
        break

     










if __name__ == "__main__":
    main()  