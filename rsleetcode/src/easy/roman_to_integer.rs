//! 13. Roman to Integer
//!
//! https://leetcode.com/problems/roman-to-integer/

use std::collections::HashMap;
use std::collections::HashSet;


pub struct Solution {
}

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let int_by_roman: HashMap<&str, i32> = [
            ("IV", 4),
            ("IX", 9),
            ("XL", 40),
            ("XC", 90),
            ("CD", 400),
            ("CM", 900),
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("L", 50),
            ("C", 100),
            ("D", 500),
            ("M", 1000),
        ].iter().cloned().collect();
        let pairs: HashSet<&str> = ["IV", "IX", "XL", "XC", "CD", "CM"].iter().cloned().collect::<HashSet<&str>>();

        let mut ret: i32 = 0;
        let mut start = 0;
        while start < s.len() {
            let mut end = start + 2;
            if end > s.len() {
                end = s.len();
            }
            let pair = &s[start..end];
            if pairs.contains(pair) {
                ret += match int_by_roman.get(pair) {
                    Some(v) => *v,
                    None => {
                        println!("No key {}", pair);
                        0
                    }

                };
                start += 2;
                continue
            };

            let mut end = start + 1;
            if end > s.len() {
                end = s.len();
            }
            ret += match int_by_roman.get(&s[start..end]) {
                Some(v) => *v,
                None => {
                    println!("No key \"{}\"", pair);
                    0
                }
            };
            start += 1
        }
        ret
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::roman_to_int("III".to_string()), 3)
    }
    #[test]
    fn test_2() {
        assert_eq!(Solution::roman_to_int("LVIII".to_string()), 58)
    }
    #[test]
    fn test_3() {
        let res = Solution::roman_to_int("MCMXCIV".to_string());
        assert_eq!(res, 1994, "Output: `{}`", res)
    }
}
