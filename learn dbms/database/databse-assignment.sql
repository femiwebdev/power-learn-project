-- This file serves as a central location for any additional SQL scripts or commands related to the database assignment.

-- Example SQL scripts for the database assignment

-- Create a new table for Authors
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Bio TEXT,
    UNIQUE(Name)
);

-- Create a new table for Categories
CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(100) NOT NULL,
    UNIQUE(CategoryName)
);

-- Create a new table for Books
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(200) NOT NULL,
    AuthorID INT,
    CategoryID INT,
    PublishedDate DATE,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

-- Create a new table for Users
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a new table for Loans
CREATE TABLE Loans (
    LoanID INT PRIMARY KEY,
    BookID INT,
    UserID INT,
    LoanDate DATE NOT NULL,
    ReturnDate DATE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Additional SQL commands can be added here as needed for the database assignment.