//! 217. Contains Duplicate
//!
//! https://leetcode.com/problems/contains-duplicate/

use std::collections::HashSet;

pub struct Solution {}

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let vec_len = nums.len();
        let uniq: HashSet<i32> = nums.into_iter().collect();
        uniq.len() != vec_len
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert!(Solution::contains_duplicate(vec![1, 2, 3, 1]))
    }
    #[test]
    fn test_2() {
        assert!(!Solution::contains_duplicate(vec![1, 2, 3, 4]))
    }
    #[test]
    fn test_3() {
        assert!(Solution::contains_duplicate(vec![
            1, 1, 1, 3, 3, 4, 3, 2, 4, 2
        ]))
    }
}
