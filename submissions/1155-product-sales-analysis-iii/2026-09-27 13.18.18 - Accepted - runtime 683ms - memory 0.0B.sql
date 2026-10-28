# Write your MySQL query statement below
with cte as (
    select product_id, year, quantity, price ,
    (rank() over (partition by product_id order by year ))as rk 
    from Sales
)
select product_id, year as first_year , quantity, price from cte where rk=1;