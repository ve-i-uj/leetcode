//! 13. Roman to Integer
//!
//! https://leetcode.com/problems/roman-to-integer/

use std::collections::HashMap;

pub struct Solution {
}

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let map: HashMap<_, _> = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]);
        let chars: Vec<char> = s.chars().collect();

        let mut res = 0;
        for i in 0..chars.len() - 1 {
            if map.get(&chars[i]).unwrap() < map.get(&chars[i + 1]).unwrap() {
                res -= map.get(&chars[i]).unwrap()
            } else {
                res += map.get(&chars[i]).unwrap()
            }
        }
        res += map.get(&chars.last().unwrap()).unwrap();

        res
        }
    }

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_0() {
        assert_eq!(Solution::roman_to_int("XIX".to_string()), 19)
    }

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
        assert_eq!(Solution::roman_to_int("MCMXCIV".to_string()), 1994)
    }
}
