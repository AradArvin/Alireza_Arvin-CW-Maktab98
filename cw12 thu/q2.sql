-- Part1
SELECT f.film_id, f.title, ca.name, f.release_year FROM film AS f
JOIN film_category AS fc
ON f.film_id = fc.film_id
JOIN category AS ca
ON fc.category_id = ca.category_id;

-- Part2
SELECT f.film_id, f.title, ca.name, f.release_year FROM film AS f
JOIN film_category AS fc
ON f.film_id = fc.film_id
JOIN category AS ca
ON fc.category_id = ca.category_id
WHERE ca.name IN ('Action','Comedy','Family');
