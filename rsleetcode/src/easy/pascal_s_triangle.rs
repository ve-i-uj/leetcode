//! 118. Pascal's Triangle
//!
//! https://leetcode.com/problems/pascal-s-triangle/

pub struct Solution {}

impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        if num_rows == 1 {
            return vec![vec![1]]
        }
        else if num_rows == 2 {
            return vec![vec![1], vec![1, 1]]
        }
        else if num_rows == 3 {
            return vec![vec![1], vec![1, 1], vec![1, 2, 1]]
        }
        let mut res = vec![vec![1], vec![1, 1], vec![1, 2, 1]];
        let mut n = 4;
        let (mut i, mut j) = (0, 1);

        while n <= num_rows {
            let mut new = vec![1];
            {
                let last = res.last().unwrap();
                while j < last.len() {
                    new.push(last[i] + last[j]);
                    i += 1;
                    j += 1;
                }
                new.push(1);
            }

            n += 1;
            i = 0;
            j = 1;

            res.push(new);
        }

        res
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let output = vec![
            vec![1],
            vec![1, 1],
            vec![1, 2, 1],
            vec![1, 3, 3, 1],
            vec![1, 4, 6, 4, 1],
        ];
        assert_eq!(Solution::generate(5), output);
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::generate(1), vec![vec![1]]);
    }
}
