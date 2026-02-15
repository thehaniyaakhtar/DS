/*
Joins
Inner Joins
*/
-- customers who have placed orders:
SELECT 
	c.customer_id,
	c.first_name,
	o.order_id,
	o.item,
	o.amount
FROM Customers c
INNER JOIN Orders o
	ON c.customer_id = o.customer_id;

