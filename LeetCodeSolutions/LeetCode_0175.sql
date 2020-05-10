# Write your MySQL query statement below
SELECT
    FirstName, LastName, City, State
FROM
    Person LEFT OUTER JOIN Address
ON
    Person.PersonID = Address.PersonID;