-- This file contains unit tests for the database schema, ensuring that tables and constraints are correctly defined.

-- Test for Users table
SELECT COUNT(*) FROM information_schema.tables 
WHERE table_name = 'Users';

-- Test for Books table
SELECT COUNT(*) FROM information_schema.tables 
WHERE table_name = 'Books';

-- Test for Loans table
SELECT COUNT(*) FROM information_schema.tables 
WHERE table_name = 'Loans';

-- Test for primary key constraint on Users table
SELECT COUNT(*) FROM information_schema.table_constraints 
WHERE table_name = 'Users' AND constraint_type = 'PRIMARY KEY';

-- Test for primary key constraint on Books table
SELECT COUNT(*) FROM information_schema.table_constraints 
WHERE table_name = 'Books' AND constraint_type = 'PRIMARY KEY';

-- Test for primary key constraint on Loans table
SELECT COUNT(*) FROM information_schema.table_constraints 
WHERE table_name = 'Loans' AND constraint_type = 'PRIMARY KEY';

-- Test for foreign key constraint in Loans table referencing Users
SELECT COUNT(*) FROM information_schema.table_constraints 
WHERE table_name = 'Loans' AND constraint_type = 'FOREIGN KEY';

-- Test for foreign key constraint in Loans table referencing Books
SELECT COUNT(*) FROM information_schema.table_constraints 
WHERE table_name = 'Loans' AND constraint_type = 'FOREIGN KEY';

-- Test for NOT NULL constraints on Users table
SELECT COUNT(*) FROM information_schema.columns 
WHERE table_name = 'Users' AND is_nullable = 'NO';

-- Test for NOT NULL constraints on Books table
SELECT COUNT(*) FROM information_schema.columns 
WHERE table_name = 'Books' AND is_nullable = 'NO';

-- Test for NOT NULL constraints on Loans table
SELECT COUNT(*) FROM information_schema.columns 
WHERE table_name = 'Loans' AND is_nullable = 'NO';

-- Test for UNIQUE constraints on Users table
SELECT COUNT(*) FROM information_schema.table_constraints 
WHERE table_name = 'Users' AND constraint_type = 'UNIQUE';

-- Test for UNIQUE constraints on Books table
SELECT COUNT(*) FROM information_schema.table_constraints 
WHERE table_name = 'Books' AND constraint_type = 'UNIQUE';