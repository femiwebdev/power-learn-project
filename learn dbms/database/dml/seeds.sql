-- seeds.sql

-- Seed data for Users table
INSERT INTO Users (id, username, email, created_at) VALUES
(1, 'john_doe', 'john@example.com', NOW()),
(2, 'jane_smith', 'jane@example.com', NOW()),
(3, 'alice_jones', 'alice@example.com', NOW());

-- Seed data for Books table
INSERT INTO Books (id, title, author, published_year, genre) VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Fiction'),
(2, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
(3, '1984', 'George Orwell', 1949, 'Dystopian');

-- Seed data for Loans table
INSERT INTO Loans (id, user_id, book_id, loan_date, return_date) VALUES
(1, 1, 2, NOW(), NULL),
(2, 2, 1, NOW(), NULL),
(3, 3, 3, NOW(), NOW() + INTERVAL '14 days');