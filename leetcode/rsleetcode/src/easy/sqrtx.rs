//! 69. Sqrtx
//!
//! https://leetcode.com/problems/sqrtx/

pub struct Solution {
}

impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        let x = x as usize;
        let mut left: usize = 0;
        let mut right = x as usize;
        let mut res: usize = 0;

        while left <= right {
            let mid = left + (right - left) / 2;
            let prediction = mid * mid;
            if prediction == x {
                return mid as i32
            }
            else if prediction < x {
                res = mid;
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        res as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::my_sqrt(4), 2)
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::my_sqrt(8), 2)
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::my_sqrt(0), 0)
    }

    #[test]
    fn test_4() {
        assert_eq!(Solution::my_sqrt(2), 1)
    }

    #[test]
    fn test_5() {
        assert_eq!(Solution::my_sqrt(9), 3)
    }

    #[test]
    fn test_6() {
        assert_eq!(Solution::my_sqrt(2147395599), 46339)
    }

}
