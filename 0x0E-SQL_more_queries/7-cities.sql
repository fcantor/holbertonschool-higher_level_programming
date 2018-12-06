-- This script creates the database hbtn_0d_usa and table cities
-- cities values: id INT, state_id INT, name VARCHAR(256)
-- If database or table already exists, no error will occur
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
    state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);