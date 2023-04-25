//! 1. Two Sum
//!
//! https://leetcode.com/problems/two-sum/

use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hash: HashMap<i32, i32> = HashMap::new();
        for (i, n) in nums.iter().enumerate() {
            let diff = target - n;
            if hash.contains_key(&diff) {
                return vec![*hash.get(&diff).unwrap(), i as i32]
            }
            hash.insert(*n, i as i32);
        }
        vec![]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![2, 7, 11, 15];
        let target = 9;
        let output = vec![0, 1];
        assert_eq!(output, Solution::two_sum(nums, target));
    }

    #[test]
    fn test_2() {
        let nums = vec![3,2,4];
        let target = 6;
        let output = vec![1, 2];
        assert_eq!(output, Solution::two_sum(nums, target));
    }

    #[test]
    fn test_3() {
        let nums = vec![3,3];
        let target = 6;
        let output = vec![0, 1];
        assert_eq!(output, Solution::two_sum(nums, target));
    }
}
