from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, sessionmaker
from sqlalchemy import Integer, String, create_engine

app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
engine = create_engine('sqlite:///new-books-collection.db')  # Use your own database URL here
Session = sessionmaker(bind=engine)

# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[str] = mapped_column(String(5), nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
Base.metadata.create_all(engine)

# CREATE RECORD
def create_record(title, author, rating):
    with Session() as session:
        new_book = Book(title=title, author=author, rating=rating)
        session.add(new_book)
        session.commit()

# DELETE RECORD
def delete_record(title):
    with Session() as session:
        book_to_delete = session.query(Book).filter(Book.title == title).first()
        if book_to_delete:
            session.delete(book_to_delete)
            session.commit()

# READ RECORDS
def read_records():
    with Session() as session:
        return session.query(Book).all()

# READ A PARTICULAR RECORD
def read_record(name):
    with Session() as session:
        book = session.query(Book).filter(Book.title == name).first()
        return book

# UPDATE RECORD BY QUERY
def update_record(name, rating):
    with Session() as session:
        book_to_update = session.query(Book).filter(Book.title == name).first()
        if book_to_update:
            book_to_update.rating = rating
            session.commit()
