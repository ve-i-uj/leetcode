//! 108. Convert Sorted Array to Binary Search Tree
//!
//! https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

use std::cell::RefCell;
use std::rc::Rc;
type OptionTree = Option<Rc<RefCell<TreeNode>>>;

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
    pub fn sorted_array_to_bst(nums: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        fn create(nums: &[i32]) -> OptionTree {
            match nums.len() {
                0 => None,
                n => {
                    let m = n / 2;
                    let mut node = TreeNode::new(nums[m]);
                    node.left = create(&nums[0..m]);
                    node.right = create(&nums[m+1..]);
                    Some(Rc::new(RefCell::new(node)))
                }
            }
        }

        create(nums.as_slice())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn to_tree(nums: Vec<Option<i32>>) -> OptionTree {
        fn create_node(i: usize, nums: &Vec<Option<i32>>) -> OptionTree {
            if i >= nums.len() {
                return None;
            };
            if let Some(val) = nums.get(i)? {
                let mut node = TreeNode::new(*val);
                node.left = create_node(i * 2 + 1, &nums);
                node.right = create_node(i * 2 + 2, &nums);
                Some(Rc::new(RefCell::new(node)))
            } else {
                return None
            }
        }
        create_node(0usize, &nums)
    }

    #[test]
    fn test_1() {
        let res = vec![Some(0), Some(-3), Some(9), Some(-10), None, Some(5)];
        let root: OptionTree = Solution::sorted_array_to_bst(vec![-10, -3, 0, 5, 9]);
        assert_eq!(to_tree(res), root);
    }

    #[test]
    fn test_2() {
        let res = vec![Some(3), Some(1)];
        let root: OptionTree = Solution::sorted_array_to_bst(vec![1, 3]);
        assert_eq!(to_tree(res), root);
    }
}
