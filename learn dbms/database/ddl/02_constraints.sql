-- Adding constraints to the tables to ensure data integrity

-- Users Table Constraints
ALTER TABLE Users
ADD CONSTRAINT PK_Users PRIMARY KEY (user_id),
ADD CONSTRAINT UQ_Users_Email UNIQUE (email);

-- Books Table Constraints
ALTER TABLE Books
ADD CONSTRAINT PK_Books PRIMARY KEY (book_id),
ADD CONSTRAINT UQ_Books_ISBN UNIQUE (isbn);

-- Loans Table Constraints
ALTER TABLE Loans
ADD CONSTRAINT PK_Loans PRIMARY KEY (loan_id),
ADD CONSTRAINT FK_Loans_User FOREIGN KEY (user_id) REFERENCES Users(user_id),
ADD CONSTRAINT FK_Loans_Book FOREIGN KEY (book_id) REFERENCES Books(book_id),
ADD CONSTRAINT CHK_Loans_Returned CHECK (returned IN (0, 1)); 

-- Additional constraints can be added as necessary for other tables in the schema.