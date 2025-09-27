CREATE INDEX idx_users_email ON Users(email);
CREATE INDEX idx_books_title ON Books(title);
CREATE INDEX idx_loans_user_id ON Loans(user_id);
CREATE INDEX idx_loans_book_id ON Loans(book_id);