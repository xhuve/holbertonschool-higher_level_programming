#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_basicFunction(self):
        self.assertEqual(max_integer([2, 4, 2, 1]), 4)

    def test_maxAtEnd(self):
        self.assertEqual(max_integer([9, 4, 2, 1]), 9)

    def test_maxAtStart(self):
        self.assertEqual(max_integer([2, 4, 2, 9]), 9)

    def test_negativeNumber(self):
        self.assertEqual(max_integer([2, -4, 2, 9]), 9)

    def test_onlyNegative(self):
        self.assertEqual(max_integer([-2, -4, -3, -9]), -2)

    def test_oneElement(self):
        self.assertEqual(max_integer([2]), 2)

    def test_emptyList(self):
        self.assertEqual(max_integer([]), None)

    def test_manyArguments(self):
        with self.assertRaises(TypeError):
            max_integer([2, 2, 5, 1], 5)