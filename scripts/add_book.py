# add_book.py
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.models import Author, Book, engine, Base
from sqlalchemy.orm import sessionmaker


Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_book(title, author_name, publication_year):
    author = session.query(Author).filter_by(name=author_name).first()

    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

        book = Book(
            title=title,
            publication_year=publication_year,
            author=author
        )
        session.add(book)
        session.commit()

# Example usage


add_book(title="The Hitchhiker's Guide to the Galaxy",
         author_name="Douglas Adams", publication_year=1979)

# Print the added book details
added_book = session.query(Book).filter_by(
    title="The Hitchhiker's Guide to the Galaxy").first()
if added_book:
    print(f"Book added successfully:\n{added_book}")
