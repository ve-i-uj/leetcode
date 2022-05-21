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

enum Direction {
    Left,
    Right,
}

struct Traverser {
    direction: Direction,
    stack: Vec<OptionTree>,
}

impl Traverser {
    fn new(root: OptionTree, direction: Direction) -> Traverser {
        let mut stack: Vec<OptionTree> = vec![];
        stack.push(root.clone());
        Traverser { direction, stack }
    }
}

#[derive(PartialEq)]
enum NodeValue {
    Value(i32),
    NoValue,
}

impl Iterator for Traverser {
    type Item = NodeValue;

    fn next(&mut self) -> Option<Self::Item> {
        match self.stack.pop() {
            Some(node) => {
                let node_value = match node {
                    Some(rc_tree) => {
                        let left = rc_tree.borrow().left.clone();
                        let right = rc_tree.borrow().right.clone();
                        if left.is_some() || right.is_some() {
                            match self.direction {
                                Direction::Left => {
                                    self.stack.push(right);
                                    self.stack.push(left);
                                },
                                Direction::Right => {
                                    self.stack.push(left);
                                    self.stack.push(right);
                                }
                            }
                        }
                        NodeValue::Value(rc_tree.borrow().val)
                    },
                    None => NodeValue::NoValue,
                };
                return Some(node_value)
            },
            None => return None
        }
    }
}

pub struct Solution {}

impl Solution {
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let tree = root.unwrap();
        let left = RefCell::borrow(&*tree).left.clone();
        let right = RefCell::borrow(&*tree).right.clone();

        let mut l_trav = Traverser::new(left, Direction::Left);
        let mut r_trav = Traverser::new(right, Direction::Right);

        let mut l_val = l_trav.next();
        let mut r_val = r_trav.next();

        while l_val.is_some() && r_val.is_some() && l_val == r_val {
            l_val = l_trav.next();
            r_val = r_trav.next();
        }

        l_val == r_val
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
