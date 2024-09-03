import unittest

from arrays_strings.merge_sort.solution import Solution


class MergeSortTest(unittest.TestCase):
    def test_merge_sort(self):
        sol = Solution()

        # Caso 1: Ejemplo dado en el problema
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        sol.merge(nums1, 3, nums2, 3)
        self.assertEqual([1,2,2,3,5,6], nums1)

        # Caso 2: nums1 está vacío
        nums1 = [0]
        nums2 = [1]
        sol.merge(nums1, 0, nums2, 1)
        self.assertEqual([1], nums1)

        # Caso 3: nums2 está vacío
        nums1 = [1]
        nums2 = []
        sol.merge(nums1, 1, nums2, 0)
        self.assertEqual([1], nums1)

        # Caso 4: Todos los elementos de nums1 son menores que los de nums2
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [4, 5, 6]
        sol.merge(nums1, 3, nums2, 3)
        self.assertEqual([1,2,3,4,5,6], nums1)

        # Caso 5: Todos los elementos de nums2 son menores que los de nums1
        nums1 = [4, 5, 6, 0, 0, 0]
        nums2 = [1, 2, 3]
        sol.merge(nums1, 3, nums2, 3)
        self.assertEqual([1,2,3,4,5,6], nums1)

        # Caso 6: Arreglos con elementos repetidos
        nums1 = [1, 1, 2, 0, 0, 0]
        nums2 = [1, 2, 3]
        sol.merge(nums1, 3, nums2, 3)
        self.assertEqual([1,1,1,2,2,3], nums1)