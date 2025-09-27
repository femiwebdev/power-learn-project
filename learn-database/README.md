# Power Learn DBMS

## Overview
The Power Learn DBMS project is designed to manage a library system, allowing users to interact with books and loans efficiently. This project includes a relational database schema that defines the structure and relationships between various entities such as Users, Books, and Loans.

## Project Structure
The project is organized into several directories, each serving a specific purpose:

- **database/**: Contains all SQL scripts for database management.
  - **ddl/**: Data Definition Language scripts for creating tables, adding constraints, and creating indexes.
  - **dml/**: Data Manipulation Language scripts for seeding and populating the database with sample data.
  - **migrations/**: Scripts for managing database schema changes over time.
  - **procedures/**: Contains stored procedures for common database operations.
  - **databse-assignment.sql**: A central location for additional SQL scripts related to the database assignment.

- **src/**: Contains the application source code.
  - **db/**: Database connection and query execution logic.
  - **models/**: Documentation for data models used in the application.

- **tests/**: Contains unit and integration tests for the database schema and queries.
  - **unit/**: Tests for verifying the correctness of the database schema.
  - **integration/**: Tests for ensuring the application interacts with the database as expected.

- **docs/**: Documentation files, including the Entity-Relationship Diagram (ERD) and schema overview.

- **docker/**: Contains Docker configuration files for containerizing the application.

- **.gitignore**: Specifies files and directories to be ignored by version control.

- **LICENSE**: Licensing information for the project.

## Setup Instructions
1. **Clone the Repository**: 
   ```
   git clone <repository-url>
   cd power_learn_dbms
   ```

2. **Database Setup**:
   - Run the SQL scripts in the `database/ddl/` directory to create the necessary tables and constraints.
   - Seed the database with initial data using the `database/dml/seeds.sql` script.

3. **Run the Application**:
   - Ensure that the database connection details are correctly configured in `src/db/connection.js`.
   - Start the application using your preferred method (e.g., Node.js).

4. **Testing**:
   - Run unit tests located in `tests/unit/` to verify the database schema.
   - Execute integration tests in `tests/integration/` to ensure proper database interactions.

## Usage
This project can be used as a foundation for building a library management system or adapted for other use cases requiring a relational database. The well-structured tables and relationships facilitate efficient data management and retrieval.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.