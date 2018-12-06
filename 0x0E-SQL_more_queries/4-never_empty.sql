-- This script creates the table id_not_null
-- id_not_null values: id INT (default value: 1), name VARCHAR(256)
-- If the table already exists, no error will occur
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);