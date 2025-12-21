-- now it is time for 10

SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id;
