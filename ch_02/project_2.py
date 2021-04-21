# Created by Ellie Le at 4/11/2021
"""
Project problem: P-2.38

Write a Python program that simulates a system that supports the functions of an e-book reader.
You should include methods for users of your system to "buy" new books, view their list of
purchased books, and read their purchased books. Your system should use actual books,
which have expired copyrights and are available on the Internet, to populate your set
of available books for users of your system to "purchase" and read.

"""

books = {'The Lord of the Rings': 12.99, 'Don Quixote': 10.99}

def load_data(title):
    """Return book data stored within a remote server."""
    pass

class Book:
    """Represent book data."""
    def __init__(self, title):
        self._title = title
        self._data = load_data(title)

class User:
    "Represent the action of e-book reader."
    def __init__(self, name, acnt):
        self._name = name
        self._acnt = acnt
        self._library = []
        self._balance = 0


    def buy_book(self, book):
        """Add book price to account balance and add book to library"""
        self._balance += books[book]
        self._library += Book(book)

    def read_book(self, book):
        """Access book within e-book reader's library"""
        book = self._library[self._library.find(book)]