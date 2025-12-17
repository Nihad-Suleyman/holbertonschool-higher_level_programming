-- now let's go on with task 15

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
