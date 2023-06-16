-- part 1
SELECT * FROM film 
WHERE rental_duration > 4;

-- part 2
SELECT * FROM film 
WHERE 2 < rental_duration AND rental_duration < 5;

-- part 3 ascending
SELECT * FROM film 
WHERE 2 < rental_duration AND rental_duration < 5
ORDER BY title ASC;

-- part 3 descending
SELECT * FROM film 
WHERE 2 < rental_duration AND rental_duration < 5
ORDER BY title DESC;