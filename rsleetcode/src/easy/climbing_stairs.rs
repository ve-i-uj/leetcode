//! 70. Climbing Stairs
//!
//! https://leetcode.com/problems/climbing-stairs/

pub struct Solution {
}

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n < 3 {
            return n
        }

        let n = n as usize;
        let mut first = 1usize;
        let mut second = 2usize;
        let mut tmp: usize;

        for _ in 2..n {
            tmp = first + second;
            first = second;
            second = tmp;
        }

        second as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_0() {
        assert_eq!(Solution::climb_stairs(1), 1)
    }

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
