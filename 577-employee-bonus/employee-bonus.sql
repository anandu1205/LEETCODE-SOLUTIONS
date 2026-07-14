-- Write your PostgreSQL query statement below
select name,bonus from employee 
left join bonus 
on bonus.empid =employee.empid
where bonus is NULL or bonus<1000