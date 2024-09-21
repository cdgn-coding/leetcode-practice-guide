import unittest
from typing import List

class TestLRUCache(unittest.TestCase):
    def test_example(self):
        lru_cache = LRUCache(2)
        lru_cache.put(1, 1)
        lru_cache.put(2, 2)
        self.assertEqual(lru_cache.get(1), 1)
        lru_cache.put(3, 3)
        self.assertEqual(lru_cache.get(2), -1)
        lru_cache.put(4, 4)
        self.assertEqual(lru_cache.get(1), -1)
        self.assertEqual(lru_cache.get(3), 3)
        self.assertEqual(lru_cache.get(4), 4)

    def test_capacity_1(self):
        lru_cache = LRUCache(1)
        lru_cache.put(1, 1)
        self.assertEqual(lru_cache.get(1), 1)
        lru_cache.put(2, 2)
        self.assertEqual(lru_cache.get(1), -1)
        self.assertEqual(lru_cache.get(2), 2)

    def test_update_existing_key(self):
        lru_cache = LRUCache(2)
        lru_cache.put(1, 1)
        lru_cache.put(2, 2)
        lru_cache.put(1, 10)
        self.assertEqual(lru_cache.get(1), 10)
        self.assertEqual(lru_cache.get(2), 2)

    def test_eviction_order(self):
        lru_cache = LRUCache(3)
        lru_cache.put(1, 1)
        lru_cache.put(2, 2)
        lru_cache.put(3, 3)
        lru_cache.put(4, 4)
        self.assertEqual(lru_cache.get(4), 4)
        self.assertEqual(lru_cache.get(3), 3)
        self.assertEqual(lru_cache.get(2), 2)
        self.assertEqual(lru_cache.get(1), -1)

    def test_large_operations(self):
        lru_cache = LRUCache(10)
        for i in range(20):
            lru_cache.put(i, i)
        for i in range(10, 20):
            self.assertEqual(lru_cache.get(i), i)
        for i in range(10):
            self.assertEqual(lru_cache.get(i), -1)

if __name__ == '__main__':
    unittest.main()