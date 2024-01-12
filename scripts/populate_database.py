# scripts/populate_database.py
import csv
from models import Author, Book, engine, Base
from sqlalchemy.orm import sessionmaker

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def populate_database():
    with open('data/library_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            author_name = row['author']
            author = session.query(Author).filter_by(name=author_name).first()

            if not author:
                author = Author(name=author_name)
                session.add(author)
                session.commit()

                book = Book(
                    title=row['title'],
                    publication_year=int(row['publication_year']),
                    author=author
                )
                session.add(book)
                session.commit()

                if __name__ == "__main__":
                    populate_database()
