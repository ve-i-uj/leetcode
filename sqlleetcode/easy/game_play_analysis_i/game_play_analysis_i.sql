-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/game-play-analysis-i/

SELECT
  a.player_id,
  MIN(a.event_date) first_login
FROM Activity a
GROUP BY a.player_id
