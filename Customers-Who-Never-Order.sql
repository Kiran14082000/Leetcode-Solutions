1# Write your MySQL query statement below
2select c.name as 'Customers' from Customers c left join Orders o on c.id = o.customerId where o.customerID is Null;