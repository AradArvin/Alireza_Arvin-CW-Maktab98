
-- Part1
SELECT district FROM address
ORDER BY district ASC LIMIT 100;

-- Part2
SELECT COUNT(district) AS row_count FROM address;

-- Part3 top3
SELECT district,
COUNT(address) AS address_count
FROM address
GROUP BY district
ORDER BY address_count DESC LIMIT 3;

-- Part4
SELECT district FROM address
WHERE district LIKE 'California' OR district LIKE 'Alberta';

-- Part5
SELECT address FROM address
WHERE district LIKE 'California' OR district LIKE 'Alberta'
OR district LIKE 'Texas' OR district LIKE 'Hamilton';

-- Part6
SELECT * FROM address
WHERE address2 IS NULL;