//! 104. Maximum Depth of Binary Tree
//!
//! https://leetcode.com/problems/maximum-depth-of-binary-tree/

use std::cell::RefCell;
use std::rc::Rc;
type Tree = Rc<RefCell<TreeNode>>;
type OptionTree = Option<Tree>;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
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

struct Solution {}

impl Solution {
    pub fn max_depth(root: OptionTree) -> i32 {
        fn count(depth: usize, root: OptionTree) -> usize {
            match root {
                Some(tree) => {
                    let l_d = count(depth + 1, tree.borrow().left.clone());
                    let r_d = count(depth + 1, tree.borrow().right.clone());
                    l_d.max(r_d)
                }
                None => depth,
            }
        }

        count(0, root) as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn create_tree(vals: Vec<Option<i32>>) -> OptionTree {
        if vals.is_empty() {
            return None;
        }

        fn create(i: usize, vals: &Vec<Option<i32>>) -> OptionTree {
            let val = *(vals.get(i)?);
            let val = val?;
            let mut tree = TreeNode::new(val);
            tree.left = create(i * 2 + 1, vals);
            tree.right = create(i * 2 + 2, vals);
            Some(Rc::new(RefCell::new(tree)))
        }

        create(0, &vals)
    }

    #[test]
    fn test_1() {
        let vals = vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)];
        let root = create_tree(vals);
        assert_eq!(Solution::max_depth(root), 3)
    }

    #[test]
    fn test_2() {
        let vals = vec![Some(1), None, Some(2)];
        let root = create_tree(vals);
        assert_eq!(Solution::max_depth(root), 2)
    }
}
