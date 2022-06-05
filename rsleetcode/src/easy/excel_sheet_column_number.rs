//! 171. Excel Sheet Column Number
//!
//! https://leetcode.com/problems/excel-sheet-column-number/

pub struct Solution {
}

impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        column_title
            .into_bytes()
            .into_iter()
            .rev()
            .enumerate()
            .fold(0, |acc, (i, u)| {
                acc + (26usize.pow(i as u32)) * (u as usize - 64)
            }) as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::title_to_number("A".to_string()), 1);
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::title_to_number("AB".to_string()), 28);
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::title_to_number("ZY".to_string()), 701);
    }

    #[test]
    fn test_4() {
        assert_eq!(Solution::title_to_number("FXSHRXW".to_string()), 2147483647);
    }
}