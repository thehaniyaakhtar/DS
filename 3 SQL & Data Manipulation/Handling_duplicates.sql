-- If duplicates rows existed
SELECT DISTINCT *
FROM Customers;

-- Removing duplicates using ROW_NUMBER
DELETE FROM Customers
WHERE customer_id IN (
    SELECT customer_id
    FROM (
        SELECT customer_id,
               ROW_NUMBER() OVER (
                   PARTITION BY first_name, last_name
                   ORDER BY customer_id
               ) AS rn
        FROM Customers
    ) t
    WHERE rn > 1
);
