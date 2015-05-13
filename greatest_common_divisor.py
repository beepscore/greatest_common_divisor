#!/usr/bin/env python3


class GreatestCommonDivisor:
    """
    Methods to return greatest common divisor of two numbers.
    """

    def greatest_common_divisor(a, b):
        """ return greatest common divisor of two numbers.
        return 0 if a <= 0 or b <= 0
        """
        if a <= 0 or b <= 0:
            return 0

        if b > a:
            # swap
            a, b = b, a

        divisor = b
        while divisor > 0:
            if a % divisor == 0 and b % divisor == 0:
                return divisor
            else:
                divisor = GreatestCommonDivisor.next_smaller_divisor(a, divisor)

    def next_smaller_divisor(number, divisor):
        index = (number // divisor) + 1
        while index <= number:
            if number % index == 0:
                return number // index
            else:
                # NOTE Python doesn't have ++ operator! Interprets ++ as two unary adds.
                index += 1
        return 1
