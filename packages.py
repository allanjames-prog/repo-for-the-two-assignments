from viola_package_assignment import *

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
library_keeper.remove_book(book1)
