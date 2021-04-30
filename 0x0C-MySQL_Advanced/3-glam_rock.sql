-- Write a SQL script that lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT band_name, CAST(formed - split AS SIGNED) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%';
