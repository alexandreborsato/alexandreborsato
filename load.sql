
-- load.sql

-- First needed to solve the problem with my.cnf file - see the my.cnf fle created:

-- mysql> SHOW VARIABLES LIKE 'secure_file_priv';
-- +------------------+-------+
-- | Variable_name    | Value |
-- +------------------+-------+
-- | secure_file_priv |       |
-- +------------------+-------+
-- 1 row in set (0.00 sec)

-- mysql> SELECT @@GLOBAL.secure_file_priv;
-- +---------------------------+
-- | @@GLOBAL.secure_file_priv |
-- +---------------------------+
-- |                           |
-- +---------------------------+
-- 1 row in set (0.00 sec)


-- Demonstrates loading data from a CSV file

-- Load a CSV of riders into the riders table
LOAD DATA INFILE '/Users/borsatoa/WorkDocs/lab/cs50/src6/mbta/red.csv'
INTO TABLE `stations`
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(name,line);
