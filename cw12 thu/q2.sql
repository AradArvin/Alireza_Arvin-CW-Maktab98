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

-- Part3
SELECT ca.name, Count(f.title) AS film_count FROM category AS ca
JOIN film_category AS fc
ON ca.category_id = fc.category_id
JOIN film AS f
ON fc.film_id = f.film_id
GROUP BY ca.name;

-- Part4
SELECT ca.name, Count(f.title) AS film_count FROM category AS ca
JOIN film_category AS fc
ON ca.category_id = fc.category_id
JOIN film AS f
ON fc.film_id = f.film_id
GROUP BY ca.name
HAVING Count(f.title) BETWEEN 60 AND 68;

-- Part5
SELECT f.film_id, f.title, ca.name AS category_name, la.name AS language FROM category AS ca
JOIN film_category AS fc
ON ca.category_id = fc.category_id
JOIN film AS f
ON fc.film_id = f.film_id
JOIN language AS la
ON f.language_id = la.language_id;

-- Part6
SELECT CONCAT(cu.first_name,' ',cu.last_name) AS customer_name, f.title AS film_name,
(re.return_date - re.rental_date) AS rental_duration FROM customer AS cu
JOIN rental AS re
ON cu.customer_id = re.customer_id
JOIN inventory AS inv
ON re.inventory_id = inv.inventory_id
JOIN film as f
ON inv.film_id = f.film_id;

-- Part7
SELECT title, length FROM film
WHERE length > (
	SELECT AVG(length)
	FROM film 
);

-- Part8
SELECT f.film_id, f.title, re.return_date FROM film AS f
JOIN inventory AS inv
ON f.film_id = inv.film_id
JOIN rental AS re
ON inv.inventory_id = re.inventory_id
WHERE re.return_date BETWEEN '2005-05-29' AND '2005-05-30';
