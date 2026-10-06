import csv
import os


class Book:
    def __init__(self, isbn: str, title: str, author: str, available: bool = True):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Checked out"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Member:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            return True
        return False


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book

    def register_member(self, member):
        if member.member_id not in self.members:
            self.members[member.member_id] = member

    def checkout(self, isbn, member_id):
        book = self.books.get(isbn)
        member = self.members.get(member_id)

        if book is None:
            print(f"Book with ISBN {isbn} not found.")
            return False

        if member is None:
            print(f"Member with ID {member_id} not found.")
            return False

        if member.borrow(book):
            print(f"{member.name} checked out '{book.title}'.")
            return True

        print(f"'{book.title}' is already checked out.")
        return False

    def checkin(self, isbn, member_id):
        book = self.books.get(isbn)
        member = self.members.get(member_id)

        if book is None:
            print(f"Book with ISBN {isbn} not found.")
            return False

        if member is None:
            print(f"Member with ID {member_id} not found.")
            return False

        if member.return_book(book):
            print(f"{member.name} returned '{book.title}'.")
            return True

        print(f"{member.name} has not borrowed '{book.title}'.")
        return False

    def list_available(self):
        return [
            book for book in self.books.values()
            if book.available
        ]

    def save_catalog(self, file_path):
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow(["isbn", "title", "author", "available"])

            for book in self.books.values():
                writer.writerow([
                    book.isbn,
                    book.title,
                    book.author,
                    book.available
                ])

        print(f"Catalog saved to {file_path}")

    def load_catalog(self, file_path):
        if not os.path.exists(file_path):
            print("No existing catalog found. Starting with an empty library.")
            return

        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                book = Book(
                    row["isbn"],
                    row["title"],
                    row["author"],
                    row["available"].lower() == "true"
                )

                self.books[book.isbn] = book

        print(f"Catalog loaded from {file_path}")


if __name__ == "__main__":
    library = Library()

    # Load existing catalog
    catalog_file = "catalog.csv"
    library.load_catalog(catalog_file)

    # Add at least three books
    library.add_book(
        Book(
            "9781593279288",
            "Python Crash Course",
            "Eric Matthes"
        )
    )

    library.add_book(
        Book(
            "9780132350884",
            "Clean Code",
            "Robert C. Martin"
        )
    )

    library.add_book(
        Book(
            "9780135957059",
            "The Pragmatic Programmer",
            "Andrew Hunt"
        )
    )

    # Register two members
    library.register_member(
        Member("M001", "Keerthana")
    )

    library.register_member(
        Member("M002", "Rahul")
    )

    print("\n=== Checkout Books ===")

    # Perform checkouts
    library.checkout("9781593279288", "M001")
    library.checkout("9780132350884", "M002")

    print("\n=== Available Books After Checkout ===")

    for book in library.list_available():
        print(book)

    print("\n=== Returning Books ===")

    # Perform returns
    library.checkin("9781593279288", "M001")

    print("\n=== Available Books After Return ===")

    for book in library.list_available():
        print(book)

    # Save updated catalog
    library.save_catalog(catalog_file)