# Write your MySQL query statement below
select customer_id from (select customer_id, count(distinct product_key) as c from  Customer group by customer_id) as sub where c>=(
select count(*) from Product)