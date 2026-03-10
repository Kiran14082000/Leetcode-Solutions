1# Write your MySQL query statement below
2select distinct(email) as 'Email' from Person group by email having count(email) <>1;