//! 118. Pascal's Triangle
//!
//! https://leetcode.com/problems/pascal-s-triangle/

pub struct Solution {}

impl Solution {
    pub fn generate(num_rows: i32) -> Vec<Vec<i32>> {
        (0..num_rows as usize).scan(Vec::new(), |state, n| {
            for i in (1..n).rev() {
                state[i] += state[i - 1];
            }
            state.push(1);
            Some(state.clone())
        }).collect()
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
