import unittest

class TestCanJump(unittest.TestCase):
    def test_example1(self):
        nums = [2, 3, 1, 1, 4]
        self.assertTrue(canJump(nums))

    def test_example2(self):
        nums = [3, 2, 1, 0, 4]
        self.assertFalse(canJump(nums))

    def test_single_element(self):
        nums = [0]
        self.assertTrue(canJump(nums))

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        self.assertFalse(canJump(nums))

    def test_large_jump(self):
        nums = [5, 0, 0, 0, 0]
        self.assertTrue(canJump(nums))

    def test_multiple_jumps(self):
        nums = [1, 2, 1, 1, 1]
        self.assertTrue(canJump(nums))

    def test_barely_reachable(self):
        nums = [1, 1, 1, 1, 1]
        self.assertTrue(canJump(nums))

    def test_unreachable(self):
        nums = [1, 1, 1, 1, 0]
        self.assertFalse(canJump(nums))

if __name__ == '__main__':
    unittest.main()