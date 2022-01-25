//! 20. Valid Parentheses
//!
//! https://leetcode.com/problems/valid-parentheses/

pub struct Solution {}

impl Solution {
    pub fn is_valid(s: String) -> bool {
        if s.len() % 2 != 0 {
            return false;
        }
        let mut stack: Vec<char> = Vec::new();
        let chs: Vec<char> = s.chars().collect();
        match chs.get(0) {
            Some(']') => return false,
            Some(')') => return false,
            Some('}') => return false,
            None => return false,
            Some(first) => stack.push(*first),
        }
        let mut i = stack.len();
        // Есть первый элемент в стеке. Остальные начинаем проверять со второго элемента
        for el in chs.iter().skip(1) {
            match el {
                ']' if i == 0 || stack[i-1] != '[' => return false,
                '}' if i == 0 || stack[i-1] != '{' => return false,
                ')' if i == 0 || stack[i-1] != '(' => return false,

                ']' if stack[i-1] == '[' => i -= 1,
                '}' if stack[i-1] == '{' => i -= 1,
                ')' if stack[i-1] == '(' => i -= 1,

                _ => {
                    stack.insert(i, *el);
                    i += 1
                }
            }
        }

        if i != 0 {
            return false;
        }

        return true;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert!(!Solution::is_valid("(".to_string()))
    }
    #[test]
    fn test_2() {
        assert!(!Solution::is_valid("(()[][]".to_string()))
    }
    #[test]
    fn test_3() {
        assert!(!Solution::is_valid("(){[[[{}()".to_string()))
    }
    #[test]
    fn test_4() {
        assert!(!Solution::is_valid("()}[]".to_string()))
    }
    #[test]
    fn test_5() {
        assert!(Solution::is_valid("()".to_string()))
    }
    #[test]
    fn test_6() {
        assert!(Solution::is_valid("()[]{}".to_string()))
    }
    #[test]
    fn test_7() {
        assert!(!Solution::is_valid("(]".to_string()))
    }
    #[test]
    fn test_8() {
        assert!(!Solution::is_valid("([)]".to_string()))
    }
    #[test]
    fn test_9() {
        assert!(Solution::is_valid("{[]}".to_string()))
    }
    #[test]
    fn test_10() {
        assert!(!Solution::is_valid("){}(".to_string()))
    }
}
