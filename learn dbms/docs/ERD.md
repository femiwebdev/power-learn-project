# Entity-Relationship Diagram (ERD) for Power Learn DBMS

## Overview
This document outlines the Entity-Relationship Diagram (ERD) for the Power Learn Database Management System (DBMS). The ERD visually represents the structure of the database, including the tables, their attributes, and the relationships between them.

## Entities and Relationships

### Users
- **Attributes**:
  - UserID (Primary Key)
  - Username (Unique, Not Null)
  - Email (Unique, Not Null)
  - PasswordHash (Not Null)
  - CreatedAt (Not Null)

### Books
- **Attributes**:
  - BookID (Primary Key)
  - Title (Not Null)
  - Author (Not Null)
  - ISBN (Unique, Not Null)
  - PublishedDate (Not Null)
  - AvailableCopies (Not Null)

### Loans
- **Attributes**:
  - LoanID (Primary Key)
  - UserID (Foreign Key, Not Null)
  - BookID (Foreign Key, Not Null)
  - LoanDate (Not Null)
  - ReturnDate

## Relationships
- **Users to Loans**: One-to-Many
  - A user can have multiple loans, but each loan is associated with one user.
  
- **Books to Loans**: One-to-Many
  - A book can be loaned out multiple times, but each loan is for one specific book.

## Diagram
(Insert ERD diagram here)

## Conclusion
This ERD serves as a blueprint for the database schema, ensuring that all entities and their relationships are clearly defined for implementation in the Power Learn DBMS project.