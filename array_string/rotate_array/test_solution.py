import unittest

class TestRotateArray(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        rotate(nums, k)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_example2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        rotate(nums, k)
        self.assertEqual(nums, [3, 99, -1, -100])

    def test_empty_array(self):
        nums = []
        k = 5
        rotate(nums, k)
        self.assertEqual(nums, [])

    def test_k_greater_than_length(self):
        nums = [1, 2, 3, 4, 5]
        k = 7
        rotate(nums, k)
        self.assertEqual(nums, [4, 5, 1, 2, 3])

    def test_k_equal_to_length(self):
        nums = [1, 2, 3, 4, 5]
        k = 5
        rotate(nums, k)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_k_equal_to_zero(self):
        nums = [1, 2, 3, 4, 5]
        k = 0
        rotate(nums, k)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()