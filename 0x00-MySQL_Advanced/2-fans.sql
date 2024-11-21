-- Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.
-- Requirements:
-- 1. Import the table dump from: metal_bands.sql.zip
-- 2. Column names in the output must be: origin and nb_fans.
-- 3. The script should work on any database.

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
