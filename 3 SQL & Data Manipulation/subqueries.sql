-- Customers who placed orders
SELECT * 
FROM Customers
WHERE customer_id IN (
	SELECT customer_id
	FROM Orders
);
-- Customers who spent above average
SELECT *
FROM (
  SELECT customer_id, SUM(amount) AS total
  FROM Orders
  GROUP BY customer_id
) t
WHERE total > (
  SELECT AVG(total)
  FROM(
    SELECT SUM(amount) AS total
    FROM Orders
	GROUP BY customer_id
  ) x
);
