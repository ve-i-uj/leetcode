//! 121. Best Time to Buy and Sell Stock
//!
//! https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

pub struct Solution {}

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_price = match prices.first() {
            Some(v) => v,
            None => return 0,
        };
        let mut profit = 0;
        for p in &prices {
            profit = profit.max(*p - min_price);
            min_price = min_price.min(p);
        }

        profit
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::max_profit(vec![7, 1, 5, 3, 6, 4]), 5)
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0)
    }
}
