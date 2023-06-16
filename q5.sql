-- Part1
SELECT * FROM customer
WHERE first_name LIKE 'Jen%';

-- Part2
SELECT * FROM customer
WHERE first_name LIKE '%er%';

-- Part3
SELECT * FROM customer
WHERE first_name LIKE '%l';

-- Part4
SELECT * FROM customer
WHERE first_name NOT LIKE 'Jen%';
