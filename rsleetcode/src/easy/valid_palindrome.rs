//! 125. Valid Palindrome
//!
//! https://leetcode.com/problems/valid-palindrome/

pub struct Solution {
}

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut iter = s.chars().filter_map(|ch| {
            match ch.is_alphanumeric() {
                true => Some(ch.to_ascii_lowercase()),
                false => None
            }
        });

        while let (Some(l), Some(r)) = (iter.next(), iter.next_back()) {
            if l != r {
                return false
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let s: String = "A man, a plan, a canal: Panama".to_string();
        assert_eq!(Solution::is_palindrome(s), true)
    }

    #[test]
    fn test_2() {
        let s: String = "race a car".to_string();
        assert_eq!(Solution::is_palindrome(s), false)
    }

    #[test]
    fn test_3() {
        let s: String = " ".to_string();
        assert_eq!(Solution::is_palindrome(s), true)
    }

    #[test]
    fn test_4() {
        let s: String = "a.".to_string();
        assert_eq!(Solution::is_palindrome(s), true)
    }

    #[test]
    fn test_5() {
        let s: String = ".a".to_string();
        assert_eq!(Solution::is_palindrome(s), true)
    }

}
