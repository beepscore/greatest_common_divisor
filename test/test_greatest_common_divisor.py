#!/usr/bin/env python3

import unittest
import greatest_common_divisor as gcd


class TestGreatestCommonDivisor(unittest.TestCase):

    def setUp(self):
        pass

    def test_greatest_common_divisor_zero(self):
        actual = gcd.GreatestCommonDivisor.greatest_common_divisor(12, 0)
        self.assertEqual(0, actual)
        actual = gcd.GreatestCommonDivisor.greatest_common_divisor(0, 13)
        self.assertEqual(0, actual)
        actual = gcd.GreatestCommonDivisor.greatest_common_divisor(-5, 13)
        self.assertEqual(0, actual)

    def test_greatest_common_divisor(self):
        actual = gcd.GreatestCommonDivisor.greatest_common_divisor(12, 8)
        self.assertEqual(4, actual)

if __name__ == "__main__":
    unittest.main()
