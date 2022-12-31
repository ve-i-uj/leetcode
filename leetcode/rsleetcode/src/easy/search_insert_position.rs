//! 35. Search Insert Position
//!
//! https://leetcode.com/problems/search-insert-position/

pub struct Solution {
}

impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        let first = match nums.first() {
            Some(el) => el,
            None => return -1,
        };
        if &target <= first {
            return 0
        }
        let last = match nums.last() {
            Some(el) => el,
            None => return -1,
        };
        if &target > last {
            return nums.len() as i32
        }
        let mut left = 0;
        let mut right = nums.len() - 1;
        while left <= right{
            let middle = left + (right - left) / 2;
            let x = nums.get(middle).unwrap();

            if x == &target {
                return middle as i32;
            }
            if &target < x {
                right = middle - 1;
            }
            else {
                left = middle + 1;
            }
        }
        return left as i32;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::search_insert(vec![1, 3, 5, 6, 7], 4), 2)
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 2), 1)
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 7), 4)
    }

    #[test]
    fn test_4() {
        assert_eq!(Solution::search_insert(vec![1, 3], 1), 0)
    }

    #[test]
    fn test_5() {
        assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 5), 2)
    }
}
