//! 125. Valid Palindrome
//!
//! https://leetcode.com/problems/valid-palindrome/

pub struct Solution {
}

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        if s.len() <= 1 {
            return true
        }
        let chars: Vec<char> = s.chars().collect();
        let mut l: i32 = 0;
        let mut r: i32 = (chars.len() - 1) as i32;
        let len = chars.len() as i32;

        while l <= r && l < len && r >= 0 {
            if !chars[l as usize].is_alphanumeric() {
                l += 1;
                continue;
            }
            if !chars[r as usize].is_alphanumeric() {
                r -= 1;
                continue;
            }
            if chars[l as usize].to_lowercase().to_string() != chars[r as usize].to_lowercase().to_string() {
                return false
            }
            l += 1;
            r -= 1;
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
