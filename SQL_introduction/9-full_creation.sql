-- Create a table

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
)

INSERT INTO IF EXISTS second_table VALUES (1, "John", 10), (2, "Ardit", 3), (3, "Bob", 14), (4, "George", 8)
