# Write your MySQL query statement below
select sell_date , 
count(Distinct product) as num_sold ,
GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
from Activities
group by sell_date;

