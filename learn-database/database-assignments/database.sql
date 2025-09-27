-- Create Actors table
CREATE TABLE Actors (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INTEGER
);

-- Create Movies table
CREATE TABLE Movies (
    id INTEGER PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    year INTEGER
);

-- Example query: Select all movies
SELECT * FROM Movies;

-- Example query: Select all actors