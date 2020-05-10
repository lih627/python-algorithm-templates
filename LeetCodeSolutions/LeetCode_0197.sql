# Write your MySQL query statement below
SELECT
    a.Id
FROM
    Weather as a,
    Weather as b
WHERE
    DateDiff(a.RecordDate, b.RecordDate) = 1 AND
    a.Temperature > b.Temperature;