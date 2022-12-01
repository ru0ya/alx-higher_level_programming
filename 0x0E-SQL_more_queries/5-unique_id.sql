-- creates a table with a default value and unique id
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, UNIQUE INDEX (id), name VARCHAR(256));
