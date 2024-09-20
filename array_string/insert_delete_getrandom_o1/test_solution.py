import unittest
import random

class RandomizedSet:
    def __init__(self):
        self.set = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.set.append(val)
        self.val_to_index[val] = len(self.set) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_val = self.set[-1]
        self.set[index] = last_val
        self.val_to_index[last_val] = index
        self.set.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.set)


class TestRandomizedSet(unittest.TestCase):
    def test_insert_remove_getRandom(self):
        randomizedSet = RandomizedSet()
        self.assertTrue(randomizedSet.insert(1))
        self.assertFalse(randomizedSet.remove(2))
        self.assertTrue(randomizedSet.insert(2))
        self.assertIn(randomizedSet.getRandom(), [1, 2])
        self.assertTrue(randomizedSet.remove(1))
        self.assertFalse(randomizedSet.insert(2))
        self.assertEqual(randomizedSet.getRandom(), 2)

    def test_insert_duplicate(self):
        randomizedSet = RandomizedSet()
        self.assertTrue(randomizedSet.insert(1))
        self.assertFalse(randomizedSet.insert(1))
        self.assertEqual(len(randomizedSet.set), 1)

    def test_remove_nonexistent(self):
        randomizedSet = RandomizedSet()
        self.assertFalse(randomizedSet.remove(1))
        self.assertTrue(randomizedSet.insert(1))
        self.assertTrue(randomizedSet.remove(1))
        self.assertFalse(randomizedSet.remove(1))

    def test_getRandom_empty(self):
        randomizedSet = RandomizedSet()
        with self.assertRaises(IndexError):
            randomizedSet.getRandom()

    def test_multiple_insert_remove_getRandom(self):
        randomizedSet = RandomizedSet()
        self.assertTrue(randomizedSet.insert(1))
        self.assertTrue(randomizedSet.insert(2))
        self.assertTrue(randomizedSet.insert(3))
        self.assertTrue(randomizedSet.remove(2))
        self.assertIn(randomizedSet.getRandom(), [1, 3])
        self.assertTrue(randomizedSet.insert(4))
        self.assertIn(randomizedSet.getRandom(), [1, 3, 4])
        self.assertTrue(randomizedSet.remove(1))
        self.assertIn(randomizedSet.getRandom(), [3, 4])

if __name__ == '__main__':
    unittest.main()