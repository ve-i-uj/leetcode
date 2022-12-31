//! 88. Merge Sorted Array
//!
//! https://leetcode.com/problems/merge-sorted-array/

pub struct Solution {}

impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        let mut m = m as usize;
        let mut n = n as usize;
        let mut write_index = m + n;

        while m > 0 && n > 0 {
            if nums1[m - 1] > nums2[n - 1] {
                nums1[write_index - 1] = nums1[m - 1];
                m -= 1;
            }
            else {
                nums1[write_index - 1] = nums2[n - 1];
                n -= 1;
            }
            write_index -= 1;
        }

        while n > 0 {
            nums1[write_index - 1] = nums2[n - 1];
            n -= 1;
            write_index -= 1;
        }

    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let mut nums1 = vec![1, 2, 3, 0, 0, 0];
        Solution::merge(&mut nums1, 3, &mut vec![2, 5, 6], 3);
        assert_eq!(*nums1, vec![1, 2, 2, 3, 5, 6])
    }

    #[test]
    fn test_2() {
        let mut nums1 = vec![1];
        Solution::merge(&mut nums1, 1, &mut vec![], 0);
        assert_eq!(*nums1, vec![1])
    }

    #[test]
    fn test_3() {
        let mut nums1 = vec![0];
        Solution::merge(&mut nums1, 0, &mut vec![1], 1);
        assert_eq!(*nums1, vec![1])
    }

    #[test]
    fn test_4() {
        let mut nums1 = vec![2, 0];
        Solution::merge(&mut nums1, 1, &mut vec![1], 1);
        assert_eq!(*nums1, vec![1, 2])
    }

    #[test]
    fn test_5() {
        let mut nums1 = vec![-1, 0, 0, 3, 3, 3, 0, 0, 0];
        Solution::merge(&mut nums1, 6, &mut vec![1, 2, 2], 3);
        assert_eq!(*nums1, vec![-1, 0, 0, 1, 2, 2, 3, 3, 3])
    }

    #[test]
    fn test_6() {
        let mut nums1 = vec![4, 0, 0, 0, 0, 0];
        Solution::merge(&mut nums1, 1, &mut vec![1, 2, 3, 5, 6], 5);
        assert_eq!(*nums1, vec![1, 2, 3, 4, 5, 6])
    }
}
