-- Group By and Aggregation
SELECT 
	c.customer_id,
	c.first_name,
SUM(o.amount) AS total_spent
FROM Customers c
LEFT JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name;

