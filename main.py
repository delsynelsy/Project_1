from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQlAlchemy database connection string
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:DDCCAA#0303@localhost/books_database"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for ORM models
Base = declarative_base()

# Define Book model
class Book(Base):
    __tablename__ = "books"

    serial_number = Column(Integer, primary_key=True, index=True)
    author = Column(String, index=True)
    book_name = Column(String, index=True)
    quantity = Column(Integer)

#Create FastAPI app
app = FastAPI()


#Endpoint to get all books
@app.get("/books/")
def get_books():
    db = SessionLocal()
    books = db.query(Book).all()
    db.close()
    return books

#Endpoint to get specific book by its serial number
@app.get("/books/{serial_number}")
def get_book(serial_number: int):
    db = SessionLocal()
    book= db.query(Book).filter(Book.serial_number== serial_number).first()
    db.close()
    return book

