# library_management_system.py
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def check_out_book(self, title):
        for book in self.books:
            if book.title == title and book.check_out():
                return f"{title} has been checked out"
        return f"{title} is not available"

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.return_book():
                return f"{title} has been returned"
        return f"{title} is not checked out"

library = Library()
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))
library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))

print(library.check_out_book("1984"))
print(library.check_out_book("1984"))
print(library.return_book("1984"))
print(library.return_book("1984"))

books_by_author = library.find_books_by_author("George Orwell")
for book in books_by_author:
    print(f"Found book: {book.title} by {book.author}")
