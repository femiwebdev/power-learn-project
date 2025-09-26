const { Client } = require('pg'); // PostgreSQL client

const client = new Client({
    user: 'your_username', // replace with your database username
    host: 'localhost', // replace with your database host
    database: 'your_database', // replace with your database name
    password: 'your_password', // replace with your database password
    port: 5432, // replace with your database port
});

const connectToDatabase = async () => {
    try {
        await client.connect();
        console.log('Connected to the database successfully');
    } catch (error) {
        console.error('Database connection error:', error.stack);
    }
};

const disconnectFromDatabase = async () => {
    try {
        await client.end();
        console.log('Disconnected from the database successfully');
    } catch (error) {
        console.error('Error disconnecting from the database:', error.stack);
    }
};

module.exports = {
    connectToDatabase,
    disconnectFromDatabase,
    client,
};