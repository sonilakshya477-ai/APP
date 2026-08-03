class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True
    def __str__(self):
        status = "Available" if self.available else "Issued"
        return f"{self.book_id} | {self.title} | {self.author} | {status}"
class Library:
    def __init__(self):
        self.books = {}
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print("Book ID already exists")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print("Book added successfully")
    def remove_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id].available:
                del self.books[book_id]
                print("Book removed successfully")
            else:
                print("Book is currently issued")
        else:
            print("Book not found")
    def display_books(self):
        if not self.books:
            print("No books in library")
        else:
            print("\nLibrary Books")
            print("-" * 60)
            for book in self.books.values():
                print(book)
    def search_book(self, keyword):
        found = False
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print("No matching books found")
    def issue_book(self, patron, book_id):
        if book_id not in self.books:
            print("Book not found")
            return
        book = self.books[book_id]
        if not book.available:
            print("Book already issued")
            return
        book.available = False
        patron.borrowed_books.append(book)
        print("Book issued successfully")
    def return_book(self, patron, book_id):
        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.available = True
                patron.borrowed_books.remove(book)
                print("Book returned successfully")
                return
        print("Book not borrowed by patron")
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []
    def display_details(self):
        print("\nPatron ID:", self.patron_id)
        print("Name:", self.name)
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(book)
        else:
            print("No books borrowed")
library = Library()
patrons = {}
while True:
    print("\n LIBRARY MANAGEMENT SYSTEM")
    print("1.Add Book")
    print("2.Remove Book")
    print("3.Display Books")
    print("4.Search Book")
    print("5.Register Patron")
    print("6.Display Patron")
    print("7.Issue Book")
    print("8.Return Book")
    print("9.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        library.add_book(book_id, title, author)
    elif choice == "2":
        book_id = input("Book ID: ")
        library.remove_book(book_id)
    elif choice == "3":
        library.display_books()
    elif choice == "4":
        keyword = input("Enter title or author: ")
        library.search_book(keyword)
    elif choice == "5":
        patron_id = input("Patron ID: ")
        if patron_id in patrons:
            print("Patron already exists")
        else:
            name = input("Name: ")
            patrons[patron_id] = Patron(patron_id, name)
            print("Patron registered successfully")
    elif choice == "6":
        patron_id = input("Patron ID: ")
        if patron_id in patrons:
            patrons[patron_id].display_details()
        else:
            print("Patron not found")
    elif choice == "7":
        patron_id = input("Patron ID: ")
        if patron_id not in patrons:
            print("Patron not found")
        else:
            book_id = input("Book ID: ")
            library.issue_book(patrons[patron_id], book_id)
    elif choice == "8":
        patron_id = input("Patron ID: ")
        if patron_id not in patrons:
            print("Patron not found")
        else:
            book_id = input("Book ID: ")
            library.return_book(patrons[patron_id], book_id)
    elif choice == "9":
        print("Thank you for using Library Management System")
        break
    else:
        print("Invalid choice")

