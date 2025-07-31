#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 5]), 5)

    def test_max_start(self):
        self.assertEqual(max_integer([9, 2, 3]), 9)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative(self):
        self.assertEqual(max_integer([-5, -3, -1]), -1)

    def test_mixed(self):
        self.assertEqual(max_integer([-1, 0, 3, -99]), 3)

    def test_all_same(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()
