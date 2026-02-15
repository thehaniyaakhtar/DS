-- Self Join
-- Customers with same last name
SELECT
	c1.first_name AS customer1,
	c2.first_name AS customer2,
	c1.last_name
FROM Customers c1
JOIN Customers c2
	ON c1.last_name = c2.last_name
	AND c1.customer_id < c2.customer_id;

