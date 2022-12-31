//! 28. Implement strStr
//!
//! https://leetcode.com/problems/implement-strstr/

pub struct Solution {
}

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle.is_empty() {
            return 0;
        }
        match haystack.find(&needle) {
            Some(index) => index as i32,
            None => -1
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::str_str("hello".to_string(), "ll".to_string()), 2)
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::str_str("aaaaa".to_string(), "bba".to_string()), -1)
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::str_str("".to_string(), "any".to_string()), -1)
    }

    #[test]
    fn test_4() {
        assert_eq!(Solution::str_str("any".to_string(), "".to_string()), 0)
    }
}
