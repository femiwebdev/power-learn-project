-- This SQL script adds relationships between tables in the database.

-- Adding foreign key constraints to establish relationships

-- Assuming the following tables exist:
-- Users (user_id PRIMARY KEY)
-- Books (book_id PRIMARY KEY)
-- Loans (loan_id PRIMARY KEY, user_id, book_id)

ALTER TABLE Loans
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id) REFERENCES Users(user_id)
ON DELETE CASCADE;

ALTER TABLE Loans
ADD CONSTRAINT fk_book
FOREIGN KEY (book_id) REFERENCES Books(book_id)
ON DELETE CASCADE;

-- Additional relationships can be added here as needed.