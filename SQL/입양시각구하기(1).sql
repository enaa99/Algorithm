SELECT HOUR(DATETIME) as HOUR, COUNT(DATETIME) as COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR>=9 AND HOUR<=19
ORDER BY HOUR ASC