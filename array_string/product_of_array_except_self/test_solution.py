import unittest

class TestProductExceptSelf(unittest.TestCase):
    def test_example1(self):
        nums = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        self.assertEqual(productExceptSelf(nums), expected_output)

    def test_example2(self):
        nums = [-1, 1, 0, -3, 3]
        expected_output = [0, 0, 9, 0, 0]
        self.assertEqual(productExceptSelf(nums), expected_output)

    def test_empty_array(self):
        nums = []
        with self.assertRaises(ValueError):
            productExceptSelf(nums)

    def test_single_element_array(self):
        nums = [5]
        with self.assertRaises(ValueError):
            productExceptSelf(nums)

    def test_large_array(self):
        nums = list(range(1, 10**5 + 1))
        expected_output = [prod(nums[:i] + nums[i+1:]) for i in range(len(nums))]
        self.assertEqual(productExceptSelf(nums), expected_output)

    def test_array_with_zeros(self):
        nums = [1, 0, 2, 0, 3]
        expected_output = [0, 0, 0, 0, 0]
        self.assertEqual(productExceptSelf(nums), expected_output)

    def test_array_with_negative_numbers(self):
        nums = [-1, -2, -3, -4]
        expected_output = [-24, -12, -8, -6]
        self.assertEqual(productExceptSelf(nums), expected_output)

def prod(nums):
    result = 1
    for num in nums:
        result *= num
    return result

if __name__ == '__main__':
    unittest.main()