-- common table expression
-- temporary result set in SQL that can be referenced within a single query
WITH customer_spending AS (
  SELECT customer_id, SUM(amount) AS total
  FROM Orders
  GROUP BY customer_id
)
SELECT * 
FROM customer_spending
WHERE total > (
  SELECT AVG(total) FROM customer_spending
);
