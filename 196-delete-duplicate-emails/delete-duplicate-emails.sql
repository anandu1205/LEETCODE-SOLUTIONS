-- Write your PostgreSQL query statement below
delete from person p
using person m 
where  p.email= m.email
and p.id>m.id