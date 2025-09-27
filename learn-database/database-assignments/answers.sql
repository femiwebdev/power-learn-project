// ...existing code...

CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    fullName VARCHAR(100),
    age INTEGER
);

INSERT INTO student (id, fullName, age) VALUES
    (1, 'Alice Smith', 18),
    (2, 'Bob Johnson', 19),
    (3, 'Carol Lee', 21);

UPDATE student
SET age = 20
WHERE id = 2;