#!/usr/bin/env python3

import unittest
import greatest_common_divisor as gcd


class TestGreatestCommonDivisor(unittest.TestCase):

    def setUp(self):
        # use tuple of tuples instead of list of tuples because data won't change
        # a, b, expected
        self.test_data = ( (12, 8, 4),
                          #(12, 9, 3)
                          )

    def test_greatest_common_divisor_zero(self):
        actual = gcd.GreatestCommonDivisor.greatest_common_divisor(12, 0)
        self.assertEqual(0, actual)
        actual = gcd.GreatestCommonDivisor.greatest_common_divisor(0, 13)
        self.assertEqual(0, actual)
        actual = gcd.GreatestCommonDivisor.greatest_common_divisor(-5, 13)
        self.assertEqual(0, actual)

    def test_greatest_common_divisor(self):
        for test_case in self.test_data:
            actual = gcd.GreatestCommonDivisor.greatest_common_divisor(test_case[0], test_case[1])
            self.assertEqual(test_case[2], actual)

if __name__ == "__main__":
    unittest.main()
