-- This file contains integration tests for the database queries, verifying that the application can interact with the database as expected.

-- Test for retrieving all users
SELECT * FROM Users;

-- Test for inserting a new user
INSERT INTO Users (username, email) VALUES ('test_user', 'test_user@example.com');

-- Test for retrieving a specific book
SELECT * FROM Books WHERE id = 1;

-- Test for loaning a book to a user
INSERT INTO Loans (user_id, book_id, loan_date, return_date) 
VALUES (1, 1, CURRENT_DATE, NULL);

-- Test for retrieving all loans for a specific user
SELECT * FROM Loans WHERE user_id = 1;

-- Test for counting the number of books in the library
SELECT COUNT(*) FROM Books;

-- Test for checking if a book is available
SELECT available FROM Books WHERE id = 1;

-- Test for returning a book
UPDATE Loans SET return_date = CURRENT_DATE WHERE user_id = 1 AND book_id = 1 AND return_date IS NULL;