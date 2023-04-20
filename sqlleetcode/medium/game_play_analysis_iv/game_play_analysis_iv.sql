-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/game-play-analysis-iv/

WITH cte AS (
  SELECT player_id,
         (DATE_ADD(MIN(event_date) OVER( PARTITION BY player_id ), INTERVAL 1 DAY) = event_date) AS mtched
  FROM Activity a
), players AS (
  SELECT COUNT(player_id) AS "value"
  FROM cte
  WHERE mtched = 1
), total AS (
  SELECT COUNT( DISTINCT player_id  ) "value"
  FROM Activity
)
SELECT ROUND( players.value / total.value, 2 ) AS "fraction"
FROM players, total
