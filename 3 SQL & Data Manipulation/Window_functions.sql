-- Window Function: caalculates a value using a "window" of rows around the current row

-- Row Number
-- Ranking orders per customer
SELECT customer_id,
item,
amount,
ROW_NUMBER() OVER(
  PARTITION BY customer_id
  ORDER BY amount DESC
)
AS row_num
FROM Orders;
-- gives each customer's order a rank

-- Rank 
-- Rank customers by spending
SELECT
	c.customer_id,
	SUM(o.amount) AS total_spent,
	RANK() OVER(
  		ORDER BY SUM(o.amount) DESC
	) AS spending_rank
FROM Customers c
JOIN Orders o
	ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

