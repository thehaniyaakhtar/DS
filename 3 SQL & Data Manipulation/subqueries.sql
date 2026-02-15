-- Customers who placed orders
SELECT * 
FROM Customers
WHERE customer_id IN (
	SELECT customer_id
	FROM Orders
);
