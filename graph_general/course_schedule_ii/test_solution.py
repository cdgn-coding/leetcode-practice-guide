import unittest

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pass

class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findOrder(2, [[1,0]]), [0,1])

    def test_example_2(self):
        result = self.solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
        self.assertTrue(result in [[0,1,2,3], [0,2,1,3]])

    def test_example_3(self):
        self.assertEqual(self.solution.findOrder(1, []), [0])

    def test_no_prerequisites(self):
        result = self.solution.findOrder(3, [])
        self.assertEqual(len(result), 3)
        self.assertEqual(set(result), {0, 1, 2})

    def test_impossible_schedule(self):
        self.assertEqual(self.solution.findOrder(2, [[1,0], [0,1]]), [])

    def test_complex_schedule(self):
        result = self.solution.findOrder(6, [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]])
        self.assertTrue(all(result.index(p[0]) > result.index(p[1]) for p in [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]))

    def test_max_courses(self):
        result = self.solution.findOrder(2000, [])
        self.assertEqual(len(result), 2000)
        self.assertEqual(set(result), set(range(2000)))

if __name__ == '__main__':
    unittest.main()