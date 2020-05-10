# Write your MySQL query statement below
select distinct a.seat_id
from
    cinema as a,
    cinema as b
where
    a.free = 1 and b.free = 1 and (a.seat_id + 1 = b.seat_id or a.seat_id - 1 = b.seat_id);