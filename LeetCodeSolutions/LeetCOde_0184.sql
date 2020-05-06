# Write your MySQL query statement below
select
    b.Name as Department,
    a.Name as Employee,
    a.Salary as Salary
from
    (select
        b.Name as Name,
        a.Salary as Salary,
        a.DID as DID
    from
        (select
            DepartmentId as DID,
            max(Salary) as Salary
        from
            Employee
        group by
            DepartmentId) as a,
        Employee as b
    where
        b.Salary = a.Salary and b.DepartmentId = a.DID) as a,
    Department as b
where
    a.DID = b.Id

