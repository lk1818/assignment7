import unittest
from unittest import TestCase
from numpy import *
from q1 import *

# This test will test the the results in question 1.
class q1_unittest(unittest.TestCase):
    def setUp(self):
        pass


    def test_1a(self):
        self.assertTrue(array_equal(Q1().a, array([[2, 7, 12],[4, 9, 14]])))


    def test_1b(self):
        self.assertTrue(array_equal(Q1().b, array([6, 7, 8, 9, 10])))


    def test_1c(self):
        self.assertTrue(array_equal(Q1().c, array([[2, 7, 12], [3, 8, 13], [4, 9, 14]])))

    def test_1d(self):
        self.assertTrue(array_equal(Q1().d, array([6, 11,  7,  3,  8,  4,  9,  5, 10])))



if __name__ == '__main__':
    unittest.main()
