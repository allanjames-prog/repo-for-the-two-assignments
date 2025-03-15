# Create a class called Book
class Book:
    # Constructor with parameters
    def __init__(self, name, author, year, color, language, pages, genre):
        self.name = name
        self.author = author
        self.year = year
        self.color = color
        self.language = language
        self.pages = pages
        self.genre = genre

    # Method to display book details
    def details(self):
        print(f"book.name: {self.name}")
        print(f"book.author: {self.author}")
        print(f"book.year: {self.year}")
        print(f"book.color: {self.color}")
        print(f"book.language: {self.language}")
        print(f"book.pages: {self.pages}")
        print(f"book.genre: {self.genre}\n")

# Create another class called Fiction that inherits behavior from Book
class Fiction(Book):
    # Method for fiction book's origin
    def origin(self):
        print("Originated from Spain")

# Create another class called Nonfiction that inherits behavior from Book
class Nonfiction(Book):
    # Method to describe when the nonfiction book was published
    def published(self):
        print("Published during World War I")

# Create another class called Author
class Author(Book):
    # Method to display awards won by the author
    def awards(self):
        return "Won the 1998 American Award"

# Create another class called Librarykeeper that manages books in the library
class Librarykeeper:
    # Constructor to initialize an empty book list
    def __init__(self):
        self.books = []

    # Method to add a book to the library
    def add_Book(self, book):
        self.books.append(book)
        print(f"Added '{book.name}' to the library")

    # Method to add an author (this function is a placeholder and does not use `author` properly)
    def add_author(self, author):
        print(f"Added an author '{author.name}' to the Book")

    # Method to search for a book by its author's name
    def search_book_by_author(self, author_name):
        for book in self.books:
            if book.author == author_name:
                print(f"Found the book '{book.name}' by {book.author}")
                return
        print(f"No book found by {author_name}")

    # Method to display the books in the library
    def display_books_in_library(self):
        print(f"There are {len(self.books)} books in the library")

    # Method to remove a book from the library
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Removed '{book.name}' from the library")
        else:
            print("The book is not in the library")

"""    These will be displayed from the other module called packages ..
Thats where they will be called to be printed
# Create book objects
book1 = Book("Enemy Called Average", "John L. Mason", 1998, "White", "English", 342, "Inspiration")
book2 = Fiction("Stuck in the Desert", "Eric Mayers", 1996, "Black", "English", 900, "Fiction")

# Display details of the books
book1.details()
book2.details()

# Create a library keeper
library_keeper = Librarykeeper()

# Add books to the library
library_keeper.add_Book(book1)
library_keeper.add_Book(book2)

# Search for a book by author
library_keeper.search_book_by_author("Eric Mayers")

# Display the books in the library
library_keeper.display_books_in_library()

# Remove a book from the library
library_keeper.remove_book(book1)"""
