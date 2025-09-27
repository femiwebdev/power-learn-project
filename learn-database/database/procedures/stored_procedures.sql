-- This file contains SQL code for stored procedures that encapsulate common database operations for reuse.

-- Stored Procedure to Add a New User
CREATE PROCEDURE AddUser (
    IN p_username VARCHAR(50),
    IN p_email VARCHAR(100),
    IN p_password VARCHAR(255)
)
BEGIN
    INSERT INTO Users (username, email, password)
    VALUES (p_username, p_email, p_password);
END;

-- Stored Procedure to Retrieve User by ID
CREATE PROCEDURE GetUserById (
    IN p_user_id INT
)
BEGIN
    SELECT * FROM Users WHERE id = p_user_id;
END;

-- Stored Procedure to Update User Email
CREATE PROCEDURE UpdateUserEmail (
    IN p_user_id INT,
    IN p_new_email VARCHAR(100)
)
BEGIN
    UPDATE Users SET email = p_new_email WHERE id = p_user_id;
END;

-- Stored Procedure to Delete a User
CREATE PROCEDURE DeleteUser (
    IN p_user_id INT
)
BEGIN
    DELETE FROM Users WHERE id = p_user_id;
END;

-- Stored Procedure to Add a New Book
CREATE PROCEDURE AddBook (
    IN p_title VARCHAR(255),
    IN p_author VARCHAR(100),
    IN p_isbn VARCHAR(20)
)
BEGIN
    INSERT INTO Books (title, author, isbn)
    VALUES (p_title, p_author, p_isbn);
END;

-- Stored Procedure to Retrieve All Books
CREATE PROCEDURE GetAllBooks ()
BEGIN
    SELECT * FROM Books;
END;

-- Stored Procedure to Loan a Book
CREATE PROCEDURE LoanBook (
    IN p_user_id INT,
    IN p_book_id INT,
    IN p_loan_date DATE,
    IN p_due_date DATE
)
BEGIN
    INSERT INTO Loans (user_id, book_id, loan_date, due_date)
    VALUES (p_user_id, p_book_id, p_loan_date, p_due_date);
END;

-- Stored Procedure to Return a Book
CREATE PROCEDURE ReturnBook (
    IN p_loan_id INT
)
BEGIN
    DELETE FROM Loans WHERE id = p_loan_id;
END;