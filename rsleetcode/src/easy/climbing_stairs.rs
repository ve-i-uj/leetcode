//! 70. Climbing Stairs
//!
//! https://leetcode.com/problems/climbing-stairs/

use std::collections::HashMap;

pub struct Solution {
}

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        let mut hash: HashMap<usize, usize> = HashMap::new();
        (Solution::fork(n as usize, &mut hash) + 1) as i32
    }

    fn fork(n: usize, hash: &mut HashMap<usize, usize>) -> usize {
        let mut res: usize = 0;
        match hash.get(&n) {
            Some(v) => return *v,
            None => (),
        }
        if n > 0 {
            res += Solution::fork(n-1, hash);
        }
        if n > 1 {
            res += Solution::fork(n-2, hash);
            res += 1;
        }

        hash.insert(n, res);
        res
    }

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::climb_stairs(2), 2)
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::climb_stairs(3), 3)
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::climb_stairs(4), 5)
    }

    #[test]
    fn test_4() {
        assert_eq!(Solution::climb_stairs(35), 14930352)
    }

    #[test]
    fn test_5() {
        assert_eq!(Solution::climb_stairs(38), 63245986)
    }

    #[test]
    fn test_6() {
        assert_eq!(Solution::climb_stairs(44), 1134903170)
    }

    #[test]
    fn test_7() {
        assert_eq!(Solution::climb_stairs(45), 1836311903)
    }

}
