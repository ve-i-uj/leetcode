//! 168. Excel Sheet Column Title
//!
//! https://leetcode.com/problems/excel-sheet-column-title/

pub struct Solution {
}

impl Solution {
    pub fn convert_to_title(column_number: i32) -> String {
        let mut n = column_number;
        let mut res = String::new();

        while n > 0 {
            n -= 1;

            let rem = (n % 26) as u8;
            let ch = (b'A' + rem) as char;

            res.insert(0, ch);

            n /= 26;
        }

        res   
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use test_case::test_case;

    #[test_case(1, "A")]
    #[test_case(28, "AB")]
    #[test_case(701, "ZY")]
    #[test_case(2147483647, "FXSHRXW")]
    #[test_case(52, "AZ")]
    fn test_excel_sheet_column_title(column_number: i32, expected: &str) {
        assert_eq!(Solution::convert_to_title(column_number), expected);
    }
}
