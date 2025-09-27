-- Drop index IdxPhone from customers table
DROP INDEX IdxPhone ON customers;

-- Create user bob with password, restricted to localhost
CREATE USER 'bob'@'localhost' IDENTIFIED BY 'S$cu3r3!';

-- Grant INSERT privilege to user bob on salesDB database
GRANT INSERT ON salesDB.* TO 'bob'@'localhost';

-- Change password for user bob
ALTER USER 'bob'@'localhost' IDENTIFIED BY 'P$55!23';