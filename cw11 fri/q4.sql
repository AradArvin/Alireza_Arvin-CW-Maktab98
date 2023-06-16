
-- Part1
SELECT district FROM address
ORDER BY district ASC LIMIT 100;

-- Part2
SELECT COUNT(district) AS row_count FROM address;