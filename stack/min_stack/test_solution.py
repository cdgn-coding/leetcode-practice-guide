import unittest

class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.minStack = MinStack()

    def test_example(self):
        self.minStack.push(-2)
        self.minStack.push(0)
        self.minStack.push(-3)
        self.assertEqual(self.minStack.getMin(), -3)
        self.minStack.pop()
        self.assertEqual(self.minStack.top(), 0)
        self.assertEqual(self.minStack.getMin(), -2)

    def test_push_and_top(self):
        self.minStack.push(5)
        self.assertEqual(self.minStack.top(), 5)
        self.minStack.push(10)
        self.assertEqual(self.minStack.top(), 10)

    def test_pop(self):
        self.minStack.push(1)
        self.minStack.push(2)
        self.minStack.pop()
        self.assertEqual(self.minStack.top(), 1)

    def test_getMin(self):
        self.minStack.push(3)
        self.minStack.push(1)
        self.minStack.push(2)
        self.assertEqual(self.minStack.getMin(), 1)
        self.minStack.pop()
        self.assertEqual(self.minStack.getMin(), 1)
        self.minStack.pop()
        self.assertEqual(self.minStack.getMin(), 3)

    def test_multiple_min_values(self):
        self.minStack.push(1)
        self.minStack.push(2)
        self.minStack.push(1)
        self.assertEqual(self.minStack.getMin(), 1)
        self.minStack.pop()
        self.assertEqual(self.minStack.getMin(), 1)

    def test_edge_cases(self):
        self.minStack.push(-2147483648)  # Minimum 32-bit integer
        self.assertEqual(self.minStack.getMin(), -2147483648)
        self.minStack.push(2147483647)  # Maximum 32-bit integer
        self.assertEqual(self.minStack.top(), 2147483647)
        self.assertEqual(self.minStack.getMin(), -2147483648)

if __name__ == '__main__':
    unittest.main()