-- 94. Binary Tree Inorder Traversal
--
-- https://leetcode.com/problems/tree-node/

WITH tree AS (
	SELECT *
	FROM Tree t
), root AS (
	SELECT tree.id, "Root" AS "type"
	FROM tree
	WHERE tree.p_id IS NULL
), leaves AS (
  SELECT tree.id, "Leaf" AS "type"
  FROM tree
  WHERE tree.id NOT IN (SELECT tree.p_id FROM tree WHERE tree.p_id IS NOT NULL)
    AND tree.id NOT IN (SELECT root.id FROM root)
), nodes AS (
  SELECT tree.id, "Inner" AS "type"
  FROM tree
  WHERE tree.id NOT IN (
      SELECT root.id
      FROM root
    UNION
      SELECT leaves.id
      FROM leaves
  )
)
  SELECT *
  FROM root
UNION
  SELECT *
  FROM nodes
UNION
  SELECT *
  FROM leaves
