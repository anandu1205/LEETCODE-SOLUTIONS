# Write your MySQL query statement below
delete p from person p
join person m on p.email=m.email
where p.id>m.id
