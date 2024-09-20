import unittest

class TestSolution(unittest.TestCase):
    def test_jump(self):
        solution = Solution()

        nums1 = [2, 3, 1, 1, 4]
        self.assertEqual(solution.jump(nums1), 2)

        nums2 = [2, 3, 0, 1, 4]
        self.assertEqual(solution.jump(nums2), 2)

        nums3 = [1, 2, 3]
        self.assertEqual(solution.jump(nums3), 2)

        nums4 = [1, 1, 1, 1]
        self.assertEqual(solution.jump(nums4), 3)

        nums5 = [1]
        self.assertEqual(solution.jump(nums5), 0)

if __name__ == '__main__':
    unittest.main()