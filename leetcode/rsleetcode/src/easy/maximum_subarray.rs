//! 53. Maximum Subarray
//!
//! https://leetcode.com/problems/maximum-subarray/

use std::cmp;

pub struct Solution {
}

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut global_maximum = i32::MIN;
        let mut local_maximum = 0;

        for x in nums {
            local_maximum = cmp::max(x, x + local_maximum);
            global_maximum = cmp::max(local_maximum, global_maximum);
        }

        global_maximum
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::max_sub_array(vec![-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::max_sub_array(vec![1]), 1)
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::max_sub_array(vec![5, 4, -1, 7, 8]), 23)
    }

    #[test]
    fn test_4() {
        assert_eq!(Solution::max_sub_array(vec![-5, -4, -1, -7, -8]), -1)
    }

}
