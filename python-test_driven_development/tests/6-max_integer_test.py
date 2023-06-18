#!/usr/bin/python3
"""
Unittest for max integers([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def EmptyList(self):
        empy = []
        self.assertIsNonee(max_integer(empty), None)

    def emptyString(self):
        self.assertIsNonee(max_integer(""), None)

    def SingleElement(self):
        sElement = [5]
        self.assertEqual(max_integer(sElement), 5)

    def ordererList(self):
        orderer = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordererList), 4)

    def unordererList(self):
        unorderer = [1, 3, 4, 2]
        self.assertEqual(max_integer(unorderer), 4)

if __name__ == '__main__':
    unittest.main()
