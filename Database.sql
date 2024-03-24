--Connect to PostgreSQL
CREATE DATABASE books_database;

--Connect to the newly created database
\c books_database;

--Create a table for storing books
CREATE TABLE books (
    serial_number SERIAL PRIMARY KEY,
    author VARCHAR(100),
    book_name VARCHAR(100),
    quantity INTEGER
);


-- Insert some sample data
INSERT INTO books (author, book_name,quantity)
VALUES 
    ('Guido van Rossum', 'Python Programming for Beginners', 10),
    ('Eric Matthes', 'Python Crash Course', 15),
    ('Mark Lutz', 'Learning Python', 8);