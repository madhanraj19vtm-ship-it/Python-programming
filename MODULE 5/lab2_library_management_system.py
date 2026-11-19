# MODULE 5 - LAB 2: Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if any(existing.book_id == book.book_id for existing in self.books):
            print("A book with this ID already exists.")
            return
        self.books.append(book)
        print("Book added successfully.")

    def display_books(self):
        if not self.books:
            print("No books are available in the library.")
            return

        print("\n===== LIBRARY BOOKS =====")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(
                f"ID: {book.book_id} | Title: {book.title} | "
                f"Author: {book.author} | Status: {status}"
            )

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_borrowed:
                    print("This book is already borrowed.")
                else:
                    book.is_borrowed = True
                    print(f'You have borrowed "{book.title}".')
                return
        print("Book ID not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    print("This book was not borrowed.")
                else:
                    book.is_borrowed = False
                    print(f'You have returned "{book.title}".')
                return
        print("Book ID not found.")


def main():
    library = Library()

    # Add a few initial books for demonstration.
    library.add_book(Book("B101", "Python Basics", "John Smith"))
    library.add_book(Book("B102", "Learning OOP", "Mary Jones"))

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            book_id = input("Enter book ID: ").strip()
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            library.add_book(Book(book_id, title, author))
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            library.borrow_book(input("Enter book ID to borrow: ").strip())
        elif choice == "4":
            library.return_book(input("Enter book ID to return: ").strip())
        elif choice == "5":
            print("Exiting Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
