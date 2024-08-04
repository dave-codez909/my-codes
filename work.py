from datetime import datetime

class LibraryBook:
    def __init__(self, title, author, publication_date, due_date, borrower):
        self.title = title
        self.author = author
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d")
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.borrower = borrower
        self.is_available = True

    def is_overdue(self):
        current_date = datetime.now()
        return self.due_date < current_date

    def display_details(self):
        """
        Print book details
        """
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Date: {self.publication_date.strftime('%Y-%m-%d')}")
        print(f"Due Date: {self.due_date.strftime('%Y-%m-%d')}")
        print(f"Borrower: {self.borrower}")

    def update_due_date(self, new_due_date):
        """
        Update the due date to a new date.
        """
        self.due_date = datetime.strptime(new_due_date, "%Y-%m-%d")

book = LibraryBook("things fall apart", "Chinua Achebe", "1958-06-08", "2023-08-10", "david")

print("Is the book overdue?", book.is_overdue())

book.display_details()

book.update_due_date("2023-09-10")



