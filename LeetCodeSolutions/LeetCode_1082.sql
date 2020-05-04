# Write your MySQL query statement below
select seller_id
from sales
group by seller_id
having sum(price) =
(select sum(price) as sellsum
from sales
group by seller_id
order by sellsum desc
limit 1);