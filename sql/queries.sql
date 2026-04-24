-- Revenue per product
SELECT product, SUM(total) AS revenue
FROM orders
GROUP BY product;


SELECT customer_name, SUM(total) AS revenue
FROM orders
GROUP BY customer_name
ORDER BY revenue DESC
LIMIT 3; 
