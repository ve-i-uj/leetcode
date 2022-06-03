//! 169. Majority Element
//!
//! https://leetcode.com/problems/majority-element/

pub struct Solution {}

impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut num: &i32 = nums.get(0).unwrap();
        let mut cntr = 1usize;

        for n in nums.iter().skip(1) {
            if cntr == 0 {
                num = n;
                cntr = 1;
                continue;
            }

            if n == num {
                cntr += 1;
            } else {
                cntr -= 1;
            }
        }

        *num
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::majority_element(vec![3, 2, 3]), 3);
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::majority_element(vec![2, 2, 1, 1, 1, 2, 2]), 2);
    }
}
