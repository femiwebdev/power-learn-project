const db = require('./connection');

// Function to get all users
const getAllUsers = async () => {
    const query = 'SELECT * FROM Users';
    const result = await db.query(query);
    return result.rows;
};

// Function to get a user by ID
const getUserById = async (id) => {
    const query = 'SELECT * FROM Users WHERE id = $1';
    const result = await db.query(query, [id]);
    return result.rows[0];
};

// Function to create a new user
const createUser = async (userData) => {
    const query = 'INSERT INTO Users (name, email) VALUES ($1, $2) RETURNING *';
    const result = await db.query(query, [userData.name, userData.email]);
    return result.rows[0];
};

// Function to update a user
const updateUser = async (id, userData) => {
    const query = 'UPDATE Users SET name = $1, email = $2 WHERE id = $3 RETURNING *';
    const result = await db.query(query, [userData.name, userData.email, id]);
    return result.rows[0];
};

// Function to delete a user
const deleteUser = async (id) => {
    const query = 'DELETE FROM Users WHERE id = $1 RETURNING *';
    const result = await db.query(query, [id]);
    return result.rows[0];
};

// Function to get all books
const getAllBooks = async () => {
    const query = 'SELECT * FROM Books';
    const result = await db.query(query);
    return result.rows;
};

// Function to get a book by ID
const getBookById = async (id) => {
    const query = 'SELECT * FROM Books WHERE id = $1';
    const result = await db.query(query, [id]);
    return result.rows[0];
};

// Function to create a new book
const createBook = async (bookData) => {
    const query = 'INSERT INTO Books (title, author) VALUES ($1, $2) RETURNING *';
    const result = await db.query(query, [bookData.title, bookData.author]);
    return result.rows[0];
};

// Function to update a book
const updateBook = async (id, bookData) => {
    const query = 'UPDATE Books SET title = $1, author = $2 WHERE id = $3 RETURNING *';
    const result = await db.query(query, [bookData.title, bookData.author, id]);
    return result.rows[0];
};

// Function to delete a book
const deleteBook = async (id) => {
    const query = 'DELETE FROM Books WHERE id = $1 RETURNING *';
    const result = await db.query(query, [id]);
    return result.rows[0];
};

// Function to get all loans
const getAllLoans = async () => {
    const query = 'SELECT * FROM Loans';
    const result = await db.query(query);
    return result.rows;
};

// Function to create a new loan
const createLoan = async (loanData) => {
    const query = 'INSERT INTO Loans (user_id, book_id, loan_date) VALUES ($1, $2, $3) RETURNING *';
    const result = await db.query(query, [loanData.user_id, loanData.book_id, loanData.loan_date]);
    return result.rows[0];
};

// Exporting the functions
module.exports = {
    getAllUsers,
    getUserById,
    createUser,
    updateUser,
    deleteUser,
    getAllBooks,
    getBookById,
    createBook,
    updateBook,
    deleteBook,
    getAllLoans,
    createLoan,
};