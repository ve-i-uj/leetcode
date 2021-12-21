// 9. Palindrome Number
//
// https://leetcode.com/problems/palindrome-number/


pub struct Solution {
}

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let x: String = x.to_string();
        let reversed: String = x.chars().rev().collect();
        x == reversed
    }
}

pub fn run() {
    debug_assert!(Solution::is_palindrome(121));
    debug_assert!(!Solution::is_palindrome(-121));
    debug_assert!(!Solution::is_palindrome(10));
}
