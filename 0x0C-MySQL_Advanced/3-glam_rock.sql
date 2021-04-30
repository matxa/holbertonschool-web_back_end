-- Write a SQL script that lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT band_name, (ifnull(formed, 0) - ifnull(split, 2021)) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
