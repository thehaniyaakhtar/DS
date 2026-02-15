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
