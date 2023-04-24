-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

SELECT actor_id,
       director_id
FROM ActorDirector ad
GROUP BY actor_id, director_id
HAVING COUNT(actor_id) >= 3
