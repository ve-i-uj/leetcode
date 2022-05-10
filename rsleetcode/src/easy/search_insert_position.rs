//! 35. Search Insert Position
//!
//! https://leetcode.com/problems/search-insert-position/

pub struct Solution {
}

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        -1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 5), 2)
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 2), 1)
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 7), 4)
    }

}
