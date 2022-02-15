//! 27. Remove Element
//!
//! https://leetcode.com/problems/remove-element/

pub struct Solution {
}

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut r_i: usize = 0;
        let mut w_i: usize = 0;
        let n_len = nums.len();
        while r_i < n_len {
            let el = &nums[r_i];
            if *el == val {
                r_i += 1;
                continue;
            }
            nums[w_i] = nums[r_i];
            w_i += 1;
            r_i += 1;
        }
        w_i as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let mut expected = vec![2, 2];
        let k: usize = expected.len();
        let mut nums: Vec<i32> = vec![3, 2, 2, 3];
        let res = Solution::remove_element(&mut nums, 3);
        assert_eq!(res as usize, expected.len());
        assert_eq!(nums[..k].sort(), expected[..k].sort());
    }
    #[test]
    fn test_2() {
        let mut expected = vec![0, 1, 4, 0, 3];
        let k: usize = expected.len();
        let mut nums: Vec<i32> = vec![0, 1, 2, 2, 3, 0, 4, 2];
        let res = Solution::remove_element(&mut nums, 2);
        assert_eq!(res as usize, expected.len());
        assert_eq!(nums[..k].sort(), expected[..k].sort());
    }

    #[test]
    fn test_3() {
        let mut expected: Vec<i32> = Vec::new();
        let k: usize = expected.len();
        let mut nums: Vec<i32> = vec![];
        let res = Solution::remove_element(&mut nums, 2);
        assert_eq!(res as usize, expected.len());
        assert_eq!(nums[..k].sort(), expected[..k].sort());
    }

}
