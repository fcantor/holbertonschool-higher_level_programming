-- This script lists all cities contained in the database hbtn_0d_usa
-- Results are sorted by cities.id in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
