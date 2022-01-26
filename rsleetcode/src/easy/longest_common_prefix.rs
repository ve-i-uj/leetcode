//! 14. Longest Common Prefix
//!
//! https://leetcode.com/problems/longest-common-prefix/

pub struct Solution {
}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        String::new()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let v: Vec<&str> = vec!["flower", "flow", "flight"];
        assert_eq!(Solution::longest_common_prefix(
            v.iter().map(|s| s.to_string()).collect()), "fl")
    }
    #[test]
    fn test_2() {
        let v: Vec<&str> = vec!["dog", "disk", "doom"];
        assert_eq!(Solution::longest_common_prefix(
            v.iter().map(|s| s.to_string()).collect()), "d")
    }
    #[test]
    fn test_3() {
        let v: Vec<&str> = vec!["dog", "", "doom"];
        assert_eq!(Solution::longest_common_prefix(
            v.iter().map(|s| s.to_string()).collect()), "")
    }
    #[test]
    fn test_4() {
        let v: Vec<&str> = vec!["dog", "racecar", "car"];
        assert_eq!(Solution::longest_common_prefix(
            v.iter().map(|s| s.to_string()).collect()), "")
    }
    #[test]
    fn test_5() {
        let v: Vec<&str> = vec![""];
        assert_eq!(Solution::longest_common_prefix(
            v.iter().map(|s| s.to_string()).collect()), "")
    }
    #[test]
    fn test_6() {
        let v: Vec<&str> = vec!["a"];
        assert_eq!(Solution::longest_common_prefix(
            v.iter().map(|s| s.to_string()).collect()), "a")
    }
    #[test]
    fn test_7() {
        let v: Vec<&str> = vec!["reflower", "flow", "flight"];
        assert_eq!(Solution::longest_common_prefix(
            v.iter().map(|s| s.to_string()).collect()), "")
    }
    #[test]
    fn test_8() {
        let v: Vec<&str> = vec!["ab", "a"];
        assert_eq!(Solution::longest_common_prefix(
            v.iter().map(|s| s.to_string()).collect()), "a")
    }
    #[test]
    fn test_9() {
        let v: Vec<&str> = vec!["flower", "flower", "flower", "flower"];
        assert_eq!(Solution::longest_common_prefix(
            v.iter().map(|s| s.to_string()).collect()), "flower")
    }
}
