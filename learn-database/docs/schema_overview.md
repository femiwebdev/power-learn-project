# Database Schema Overview

## Overview
This document provides an overview of the database schema for the Power Learn DBMS project. It outlines the main tables, their fields, and the relationships between them.

## Tables

### Users
- **user_id** (INT, PRIMARY KEY, NOT NULL): Unique identifier for each user.
- **username** (VARCHAR(50), UNIQUE, NOT NULL): The username of the user.
- **email** (VARCHAR(100), UNIQUE, NOT NULL): The email address of the user.
- **password** (VARCHAR(255), NOT NULL): The hashed password of the user.
- **created_at** (TIMESTAMP, NOT NULL): The date and time when the user was created.

### Books
- **book_id** (INT, PRIMARY KEY, NOT NULL): Unique identifier for each book.
- **title** (VARCHAR(255), NOT NULL): The title of the book.
- **author** (VARCHAR(100), NOT NULL): The author of the book.
- **isbn** (VARCHAR(20), UNIQUE, NOT NULL): The ISBN number of the book.
- **published_date** (DATE): The date when the book was published.

### Loans
- **loan_id** (INT, PRIMARY KEY, NOT NULL): Unique identifier for each loan.
- **user_id** (INT, FOREIGN KEY, NOT NULL): References the user who borrowed the book.
- **book_id** (INT, FOREIGN KEY, NOT NULL): References the book that was borrowed.
- **loan_date** (DATE, NOT NULL): The date when the book was borrowed.
- **return_date** (DATE): The date when the book was returned.

## Relationships
- **Users to Loans**: One-to-Many
  - A user can have multiple loans, but each loan is associated with only one user.
  
- **Books to Loans**: One-to-Many
  - A book can be loaned out multiple times, but each loan is associated with only one book.

## Conclusion
This schema provides a solid foundation for managing users, books, and loans within the Power Learn DBMS project. The defined relationships ensure data integrity and facilitate efficient data retrieval.