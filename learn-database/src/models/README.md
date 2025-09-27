# Data Models Documentation

This README file provides an overview of the data models used in the Power Learn Database Management System (DBMS) project. The models represent the core entities of the application and their relationships.

## Models Overview

### 1. Users
- **Description**: Represents the users of the application.
- **Fields**:
  - `user_id`: INT, PRIMARY KEY, AUTO_INCREMENT
  - `username`: VARCHAR(50), UNIQUE, NOT NULL
  - `email`: VARCHAR(100), UNIQUE, NOT NULL
  - `password`: VARCHAR(255), NOT NULL
  - `created_at`: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP

### 2. Books
- **Description**: Represents the books available in the system.
- **Fields**:
  - `book_id`: INT, PRIMARY KEY, AUTO_INCREMENT
  - `title`: VARCHAR(255), NOT NULL
  - `author`: VARCHAR(100), NOT NULL
  - `isbn`: VARCHAR(20), UNIQUE, NOT NULL
  - `published_date`: DATE
  - `created_at`: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP

### 3. Loans
- **Description**: Represents the loan records for books borrowed by users.
- **Fields**:
  - `loan_id`: INT, PRIMARY KEY, AUTO_INCREMENT
  - `user_id`: INT, FOREIGN KEY REFERENCES Users(user_id), NOT NULL
  - `book_id`: INT, FOREIGN KEY REFERENCES Books(book_id), NOT NULL
  - `loan_date`: TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP
  - `return_date`: TIMESTAMP

## Relationships

- **Users to Loans**: One-to-Many
  - A user can have multiple loans, but each loan is associated with only one user.

- **Books to Loans**: One-to-Many
  - A book can be loaned out multiple times, but each loan record refers to only one book.

## Conclusion

This document serves as a guide to understanding the data models within the Power Learn DBMS project. Each model is designed to ensure data integrity and facilitate efficient data management through well-defined relationships.