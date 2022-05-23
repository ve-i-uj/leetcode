//! 101. Symmetric Tree
//!
//! https://leetcode.com/problems/symmetric-tree/

use std::cell::RefCell;
use std::rc::Rc;
type Tree = Rc<RefCell<TreeNode>>;
type OptionTree = Option<Tree>;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: OptionTree,
    pub right: OptionTree,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

pub struct Solution {}

impl Solution {
    pub fn is_symmetric(root: OptionTree) -> bool {
        fn compare(left: OptionTree, right: OptionTree) -> bool {
            if left.is_none() && right.is_none() {
                return true
            };

            if let (Some(l_node), Some(r_node)) = (left, right) {
                if l_node.borrow().val != r_node.borrow().val {
                    return false
                };
                compare(l_node.borrow().left.clone(), r_node.borrow().right.clone())
                && compare(r_node.borrow().left.clone(), l_node.borrow().right.clone())
            } else {
                false
            }
        }

        let root = root.unwrap();
        let res = compare(root.borrow().left.clone(), root.borrow().right.clone());
        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn create_tree(vals: &Vec<Option<i32>>) -> OptionTree {
        if vals.is_empty() {
            return None;
        }

        fn create(i: usize, vals: &Vec<Option<i32>>) -> OptionTree {
            if i >= vals.len() || vals[i].is_none() {
                return None;
            }
            let mut node = TreeNode::new(vals[i].unwrap());
            node.left = create(i * 2 + 1, vals);
            node.right = create(i * 2 + 2, vals);
            Some(Rc::new(RefCell::new(node)))
        }

        create(0, &vals)
    }

    #[test]
    fn test_1() {
        let vals = vec![
            Some(1),
            Some(2),
            Some(2),
            Some(3),
            Some(4),
            Some(4),
            Some(3),
        ];
        let root = create_tree(&vals);

        assert_eq!(Solution::is_symmetric(root), true);
    }

    #[test]
    fn test_2() {
        let vals = vec![Some(1), Some(2), Some(2), None, Some(3), None, Some(3)];
        let root = create_tree(&vals);

        assert_eq!(Solution::is_symmetric(root), false);
    }
}
