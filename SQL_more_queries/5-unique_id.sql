-- Create table unique_id 
-- id INT default value 1 must be unique, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id(id INT default 1 UNIQUE, name VARCHAR(256))