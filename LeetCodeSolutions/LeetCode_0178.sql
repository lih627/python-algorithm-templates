# Write your MySQL query statement below
select
    score as 'Score',
    dense_rank() over(order by score desc) as 'Rank'
from
    scores;