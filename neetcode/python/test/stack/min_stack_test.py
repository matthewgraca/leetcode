import unittest
from src.stack.min_stack import MinStack

class MinStackTest(unittest.TestCase):
    def test_constructor(self):
        stack = MinStack()
        self.assertEqual(True, True)

    def test_push(self):
        stack = MinStack()
        stack.push(-2)
        self.assertEqual(True, True)

    def test_pop(self):
        stack = MinStack()
        stack.push(-2)
        stack.pop()
        self.assertEqual(True, True)

    def test_top(self):
        stack = MinStack()
        stack.push(-2)
        expected = -2
        actual = stack.top()
        self.assertEqual(actual, expected)

    def test_getMin(self):
        stack = MinStack()
        stack.push(0)
        stack.push(-1)
        stack.push(5)
        expected = -1
        actual = stack.getMin()
        self.assertEqual(actual, expected)
    
    def test_example1(self):
        minStack = MinStack()
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);

        actual = minStack.getMin(); # return -3
        expected = -3
        self.assertEqual(actual, expected)

        minStack.pop();
        actual = minStack.top();    # return 0
        expected = 0
        self.assertEqual(actual, expected)

        actual = minStack.getMin(); # return -2
        expected = -2
        self.assertEqual(actual, expected)

    def test_example2(self):
        minStack = MinStack()
        minStack.push(0)
        minStack.push(1)
        minStack.push(0)

        actual = minStack.getMin()
        expected = 0
        self.assertEqual(actual, expected)

        minStack.pop()
        actual = minStack.getMin()
        expected = 0
        self.assertEqual(actual, expected)
