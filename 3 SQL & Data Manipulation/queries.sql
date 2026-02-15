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

/*
Left Joins
*/
-- All customers + their orders:
SELECT 
	c.customers_id,
	c.first_name,
	o.orer_id,
	o.item
FROM Customer c
LEFT JOIN Orders o
	ON c.customers_id = o.customers_id
;
/*
Full Outer Joins
*/
SELECT 
c.first_name,
o.order_id
FROM Customers c
FULL OUTER JOIN Orders o
ON c.customer_id = o.customer_id
;
-- JOIN 3 Tables
SELECT 
	c.first_name,
	o.item,
	s.status
FROM Customers c
LEFT JOIN Orders o 
	ON c.customer_id = o.customer_id
LEFT JOIN Shippings s
	ON c.customer_id = s.customer;



