-- List all the cities of california tha can be found
-- In the database hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;