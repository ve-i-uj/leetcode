-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/game-play-analysis-iv/

WITH total AS (
  SELECT COUNT( DISTINCT(player_id) ) AS "value"
  FROM Activity a
), players AS (
  SELECT COUNT(a1.player_id) AS "value"
  FROM Activity a1
    JOIN (
      SELECT player_id,
             MIN(event_date) AS "event_date"
      FROM Activity a
      GROUP BY player_id
    ) a2 ON a1.player_id = a2.player_id
      AND a1.event_date = DATE_ADD(a2.event_date, INTERVAL 1 DAY)
)
SELECT ROUND( p.value / t.value, 2 ) AS "fraction"
FROM players p,
     total t
