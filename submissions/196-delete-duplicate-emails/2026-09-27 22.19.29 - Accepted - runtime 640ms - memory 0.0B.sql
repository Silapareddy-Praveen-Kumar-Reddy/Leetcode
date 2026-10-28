# Write your MySQL query statement below
delete from person where id in (
    select id from (select id, row_number() over (partition
    by email order by id) as rn from Person ) s
    where rn >1
);
