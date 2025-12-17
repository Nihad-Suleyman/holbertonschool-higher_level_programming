-- now let's go for 16

SELECT score, name FROM second_table WHERE name IS NOT NULL OR name != "" ORDER BY score DESC;
