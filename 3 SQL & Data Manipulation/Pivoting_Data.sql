SELECT
  SUM(CASE WHEN country = "USA" THEN amount END) AS USA_total,
  SUM(CASE WHEN country = "UK" THEN amount END) AS UK_total,
  SUM(CASE WHEN country = "UAE" THEN amount END) AS UAE_total
FROM Customers c
JOIN Orders O
  ON c.customer_id = o.customer_id
;
