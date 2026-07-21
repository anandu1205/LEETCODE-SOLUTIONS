# Write your MySQL query statement below
SELECT id, movie, description, rating
FROM cinema
WHERE description != 'Boring'
  AND MOD(id, 2) = 1
ORDER BY rating DESC;