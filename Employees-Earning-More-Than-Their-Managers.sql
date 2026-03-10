1# Write your MySQL query statement below
2select  name as 'Employee' from Employee e where salary>(select salary from employee where id=e.managerId);
3