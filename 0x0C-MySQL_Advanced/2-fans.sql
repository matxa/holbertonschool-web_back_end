-- Write a SQL script that ranks country origins of bands
-- ordered by the number of (non-unique) fans
SELECT
    origin
    RANK() OVER (
        ORDER BY fans NOT UNIQUE
    ) nb_fans
FROM metal_bands;
