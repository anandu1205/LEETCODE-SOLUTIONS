# Write your MySQL query statement below
select name as Customers from Customers 
left join orders 
on customers.id=orders.customerid
where orders.customerid is NULL