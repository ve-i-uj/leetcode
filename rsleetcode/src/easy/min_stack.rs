//! 155. Min Stack
//!
//! https://leetcode.com/problems/min-stack/

use std::collections::VecDeque;

#[derive(Debug, PartialEq, Eq)]
pub struct MinStack {
    stack: Vec<i32>,
    ordered: VecDeque<i32>,
}

impl MinStack {

    fn new() -> Self {
        MinStack {
            stack: vec![],
            ordered: VecDeque::new(),
        }
    }

    fn push(&mut self, val: i32) {
        if let Some(last) = self.ordered.back() {
            if last <= &val {
                self.ordered.push_back(val);
                self.stack.push(val);
                return;
            }
        }
        if let Some(first) = self.ordered.front() {
            if first >= &val {
                self.ordered.push_front(val);
                self.stack.push(val);
                return
            }
        }
        let i = match self.ordered.binary_search(&val) {
            Ok(i) => i,
            Err(i) => i,
        };
        self.ordered.insert(i, val);
        self.stack.push(val);
    }

    fn pop(&mut self) {
        let val = self.stack.pop().unwrap();
        if let Some(last) = self.ordered.back() {
            if &val == last {
                self.ordered.pop_back();
                return;
            }
        }
        if let Some(first) = self.ordered.front() {
            if &val == first {
                self.ordered.pop_front();
                return
            }
        }
        let i = self.ordered.binary_search(&val).ok().unwrap();
        self.ordered.remove(i);
    }

    fn top(&self) -> i32 {
        self.stack.last().unwrap().clone()
    }

    fn get_min(&self) -> i32 {
        self.ordered.front().unwrap().clone()
    }
}

#[cfg(test)]
mod tests {
    use super::MinStack;

    #[test]
    fn test_1() {
        let mut stack = MinStack::new();
        stack.push(-2);
        stack.push(0);
        stack.push(-3);

        assert_eq!(stack.get_min(), -3);

        stack.pop();

        assert_eq!(stack.top(), 0);
        assert_eq!(stack.get_min(), -2);
    }

    #[test]
    fn test_2() {
        let mut stack = MinStack::new();
        stack.push(-2);
        stack.push(0);
        stack.push(-1);

        assert_eq!(stack.get_min(), -2);
        assert_eq!(stack.top(), -1);

        stack.pop();

        assert_eq!(stack.get_min(), -2);
    }
}
