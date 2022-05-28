//! 155. Min Stack
//!
//! https://leetcode.com/problems/min-stack/

#[derive(Debug, Default)]
struct MinStack {
    stack: Vec<(i32, i32)> // (val, min_val)
}

impl MinStack {

    fn new() -> Self {
        MinStack::default()
    }

    fn push(&mut self, val: i32) {
        let mut min = val;
        if let Some((_, min_val)) = self.stack.last() {
            min = min.min(min_val.clone());
        };
        self.stack.push((val, min));
    }

    fn pop(&mut self) {
        self.stack.pop();
    }

    fn top(&self) -> i32 {
        self.stack.last().unwrap().0
    }

    fn get_min(&self) -> i32 {
        self.stack.last().unwrap().1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

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
