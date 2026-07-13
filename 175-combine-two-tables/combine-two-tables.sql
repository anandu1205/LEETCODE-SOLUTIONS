# Write your MySQL query statement below
select firstName,lastName,state,city from 
Person LEFT JOIN Address 
on person.personid=address.personid

