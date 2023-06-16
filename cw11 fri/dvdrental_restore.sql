-- part 1
SELECT * FROM film 
WHERE rental_duration > 4;

-- part 2
SELECT * FROM film 
WHERE 2 < rental_duration AND rental_duration < 5;

-- part 3 order by title ascending
SELECT * FROM film 
WHERE 2 < rental_duration AND rental_duration < 5
ORDER BY title ASC;

-- part 3 order by title descending
SELECT * FROM film 
WHERE 2 < rental_duration AND rental_duration < 5
ORDER BY title DESC;

-- part 3 order by rental_duration ascending
SELECT * FROM film 
WHERE 2 < rental_duration AND rental_duration < 5
ORDER BY rental_duration ASC;

-- part 3 order by last_update descending
SELECT * FROM film 
WHERE 2 < rental_duration AND rental_duration < 5
ORDER BY last_update DESC;

-- part 3 order by last_update ascending
SELECT * FROM film 
WHERE 2 < rental_duration AND rental_duration < 5
ORDER BY last_update ASC;