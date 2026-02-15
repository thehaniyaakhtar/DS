-- Group By and Aggregation
SELECT 
	c.customer_id,
	c.first_name,
SUM(o.amount) AS total_spent
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name;

-- Count order per country
SELECT 
	c.country,
COUNT(o.order_id) AS total_orders
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.country
;

-- Having 
SELECT
c.customer_id,
SUM(o.amount) AS total_spent
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id
HAVING SUM(o.amount) > 500
;





