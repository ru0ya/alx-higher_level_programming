-- lists number of records with same values
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
HAVING COUNT(*) >= 1;
