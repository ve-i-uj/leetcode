//! 190. Reverse Bits
//!
//! https://leetcode.com/problems/reverse-bits/

use std::fmt::Binary;

pub struct Solution {
}

impl Solution {
    pub fn reverse_bits(x: u32) -> u32 {
        let s = format!("{x:b}");
        let s = s.chars().rev().collect::<String>();
        let s = format!("{s:0<32}");
        u32::from_str_radix(&s, 2).unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let input = u32::from_str_radix("00000010100101000001111010011100", 2);
        assert_eq!(Solution::reverse_bits(input.unwrap()), 964176192);
    }

    #[test]
    fn test_2() {
        let input = u32::from_str_radix("11111111111111111111111111111101", 2);
        assert_eq!(Solution::reverse_bits(input.unwrap()), 3221225471);
    }
}
