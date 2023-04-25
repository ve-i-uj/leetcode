//! 9. Palindrome Number
//!
//! https://leetcode.com/problems/palindrome-number/

pub struct Solution {
}

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x.is_negative() || (x != 0 && x % 10 == 0) {
            return false
        }
        let mut y = x;
        let mut invert = 0;
        while y > invert {
            invert = 10 * invert + y % 10;
            y /= 10;
        }

        invert == y || invert / 10 == y
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert!(Solution::is_palindrome(121))
    }

    #[test]
    fn test_2() {
        assert!(!Solution::is_palindrome(-121))
    }

    #[test]
    fn test_3() {
        assert!(!Solution::is_palindrome(10))
    }

    #[test]
    fn test_4() {
        assert!(Solution::is_palindrome(0))
    }
}
