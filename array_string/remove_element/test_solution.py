import unittest

class TestRemoveElement(unittest.TestCase):
    def test_example1(self):
        nums = [3, 2, 2, 3]
        val = 3
        expected_nums = [2, 2]
        k = removeElement(nums, val)
        self.assertEqual(k, len(expected_nums))
        nums[:k] = sorted(nums[:k])
        self.assertEqual(nums[:k], expected_nums)

    def test_example2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expected_nums = [0, 1, 4, 0, 3]
        k = removeElement(nums, val)
        self.assertEqual(k, len(expected_nums))
        nums[:k] = sorted(nums[:k])
        self.assertEqual(nums[:k], sorted(expected_nums))

    def test_empty_array(self):
        nums = []
        val = 0
        expected_nums = []
        k = removeElement(nums, val)
        self.assertEqual(k, len(expected_nums))
        nums[:k] = sorted(nums[:k])
        self.assertEqual(nums[:k], expected_nums)

    def test_no_removal(self):
        nums = [1, 2, 3, 4, 5]
        val = 6
        expected_nums = [1, 2, 3, 4, 5]
        k = removeElement(nums, val)
        self.assertEqual(k, len(expected_nums))
        nums[:k] = sorted(nums[:k])
        self.assertEqual(nums[:k], sorted(expected_nums))

    def test_all_elements_removed(self):
        nums = [1, 1, 1, 1, 1]
        val = 1
        expected_nums = []
        k = removeElement(nums, val)
        self.assertEqual(k, len(expected_nums))
        nums[:k] = sorted(nums[:k])
        self.assertEqual(nums[:k], expected_nums)

if __name__ == '__main__':
    unittest.main()