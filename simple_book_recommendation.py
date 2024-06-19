class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

def recommend_books(books, genre):
    return [book for book in books if book.genre == genre]

def main():
    books = [
        Book("To Kill a Mockingbird", "Harper Lee", "Fiction"),
        Book("A Brief History of Time", "Stephen Hawking", "Science"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction"),
        Book("The Man Who Knew Infinity", "Robert Kanigel", "Biography")
    ]
    genre = "Fiction"
    recommended = recommend_books(books, genre)
    print(f"Books in the genre '{genre}':")
    for book in recommended:
        print(f"- {book.title} by {book.author}")

if __name__ == "__main__":
    main()
