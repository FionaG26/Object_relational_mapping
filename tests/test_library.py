# tests/test_library.py
import unittest
from models import Author, Book, Base, engine
from sqlalchemy.orm import sessionmaker
from scripts.populate_database import populate_database


class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        # Create tables before each test
        Base.metadata.create_all(engine)
        self.session = sessionmaker(bind=engine)()

        # Populate the database with sample data
        populate_database()

        def tearDown(self):
            # Drop all tables after each test
            Base.metadata.drop_all(engine)

            def test_add_book(self):
                # Test adding a new book
                from scripts.populate_database import add_book

                add_book('New Book', 'New Author', 2022)
                new_book = self.session.query(
                    Book).filter_by(title='New Book').first()
                self.assertIsNotNone(new_book)

                def test_books_by_author(self):
                    # Test retrieving books by a specific author
                    books_by_author = self.session.query(Book).join(
                        Author).filter(Author.name == 'J.R.R. Tolkien').all()
                    self.assertEqual(len(books_by_author), 2)

                    if __name__ == '__main__':
                        unittest.main()
