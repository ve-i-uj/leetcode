//! 94. Binary Tree Inorder Traversal
//!
//! https://leetcode.com/problems/binary-tree-inorder-traversal/

use std::cell::RefCell;
use std::rc::Rc;

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

pub struct Solution {}

impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut res = Vec::new();
        let mut stack = Vec::new();
        let mut root = root;

        while root.is_some() || !stack.is_empty() {
            while let Some(node) = root {
                stack.push(Rc::clone(&node));
                root = node.borrow().left.clone();
            }
            if let Some(node) = stack.pop() {
                res.push(node.borrow().val);
                root = node.borrow().right.clone();
            }
        }

        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn normalize_data(vals: &mut Vec<Option<i32>>) {
        let mut i = 0;
        let mut l_i;
        let mut r_i;
        while i < vals.len() {
            if vals[i].is_none() {
                l_i = i * 2 + 1;
                r_i = i * 2 + 2;
                if l_i < vals.len() && vals[l_i].is_some() {
                    vals.insert(l_i, None)
                }
                if r_i < vals.len() && vals[r_i].is_some() {
                    vals.insert(r_i, None)
                }
            }
            i += 1;
        }
    }

    fn from_vector(vals: Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        if vals.is_empty() {
            return None;
        }

        fn create_node(vs: &Vec<Option<i32>>, i: usize) -> Option<Rc<RefCell<TreeNode>>> {
            if i >= vs.len() {
                return None;
            }
            let val = match vs[i] {
                Some(v) => v,
                None => return None,
            };
            let mut node = TreeNode::new(val);
            node.left = create_node(vs, i * 2 + 1);
            node.right = create_node(vs, i * 2 + 2);
            Some(Rc::new(RefCell::new(node)))
        }

        create_node(&vals, 0)
    }

    #[test]
    fn test_1() {
        let mut vals = vec![Some(1), None, Some(2), Some(3)];
        normalize_data(&mut vals);
        let root = from_vector(vals);
        assert_eq!(Solution::inorder_traversal(root), vec![1, 3, 2]);
    }

    #[test]
    fn test_2() {
        let mut vals = vec![];
        normalize_data(&mut vals);
        let root = from_vector(vals);
        assert_eq!(Solution::inorder_traversal(root), vec![]);
    }

    #[test]
    fn test_3() {
        let mut vals = vec![Some(1)];
        normalize_data(&mut vals);
        let root = from_vector(vals);
        assert_eq!(Solution::inorder_traversal(root), vec![1]);
    }

    #[test]
    fn test_4() {
        let mut vals = vec![Some(1), Some(2), Some(3), Some(4)];
        normalize_data(&mut vals);
        let root = from_vector(vals);
        assert_eq!(Solution::inorder_traversal(root), vec![4, 2, 1, 3]);
    }

    #[test]
    fn test_5() {
        let mut vals = vec![
            Some(1), Some(2), Some(3), Some(4), Some(5), None, Some(7)
        ];
        normalize_data(&mut vals);
        let root = from_vector(vals);
        assert_eq!(Solution::inorder_traversal(root), vec![4, 2, 5, 1, 3, 7]);
    }
}
