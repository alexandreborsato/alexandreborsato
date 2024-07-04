# sql to create a new contacts table
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
    );

# Write your MySQL query statement below
SELECT
    name
    ,population
    ,area
    FROM World
    WHERE area > 3000000
    OR population > 25000000;