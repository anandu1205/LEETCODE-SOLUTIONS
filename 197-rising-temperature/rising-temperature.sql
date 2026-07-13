-- Write your PostgreSQL query statement below
select w.id
from weather w 
join weather m 
on w.recordDate=m.recordDate+INTERVAL '1 day'
where w.temperature>m.temperature
