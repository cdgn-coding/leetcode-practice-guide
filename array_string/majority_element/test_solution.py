import unittest

class TestMajorityElement(unittest.TestCase):
    def test_example1(self):
        nums = [3, 2, 3]
        self.assertEqual(majorityElement(nums), 3)

    def test_example2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(majorityElement(nums), 2)

    def test_single_element(self):
        nums = [5]
        self.assertEqual(majorityElement(nums), 5)

    def test_two_elements_same(self):
        nums = [2, 2]
        self.assertEqual(majorityElement(nums), 2)

    def test_two_elements_different(self):
        nums = [2, 3]
        self.assertIn(majorityElement(nums), [2, 3])

    def test_large_input(self):
        nums = [1] * 25000 + [2] * 25001
        self.assertEqual(majorityElement(nums), 2)

if __name__ == '__main__':
    unittest.main()