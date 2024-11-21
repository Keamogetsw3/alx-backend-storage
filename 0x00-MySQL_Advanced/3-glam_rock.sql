-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity.
-- Requirements:
-- 1. Import the table dump from: metal_bands.sql.zip.
-- 2. Column names in the output must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE())).
-- 3. Use the attributes `formed` and `split` to compute the lifespan.
-- 4. The script should work on any database.

SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;
