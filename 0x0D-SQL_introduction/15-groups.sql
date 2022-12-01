-- lists number of records with same values
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
HAVING COUNT(*) >= 1;
