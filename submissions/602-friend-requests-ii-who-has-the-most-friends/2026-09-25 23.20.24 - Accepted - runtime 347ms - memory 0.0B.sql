
with cte as
((SELECT requester_id as id from RequestAccepted) UNION ALL ( select accepter_id  as id from RequestAccepted)) 
select  id, count(id)as num  from cte group by id order by count(id) desc limit 1 OFFSET 0;