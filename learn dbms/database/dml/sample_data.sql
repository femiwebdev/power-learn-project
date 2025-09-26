INSERT INTO Users (username, email, password) VALUES
('john_doe', 'john@example.com', 'password123'),
('jane_smith', 'jane@example.com', 'password456'),
('alice_jones', 'alice@example.com', 'password789');

INSERT INTO Books (title, author, published_year, isbn) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, '9780743273565'),
('To Kill a Mockingbird', 'Harper Lee', 1960, '9780061120084'),
('1984', 'George Orwell', 1949, '9780451524935');

INSERT INTO Loans (user_id, book_id, loan_date, return_date) VALUES
(1, 1, '2023-01-15', '2023-01-22'),
(1, 2, '2023-02-01', '2023-02-08'),
(2, 1, '2023-03-05', '2023-03-12'),
(3, 3, '2023-04-10', NULL);