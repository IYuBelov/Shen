from unittest import TestCase

from values_1.without_array_1_1 import swap, swap_numbers, pow, super_pow, multiply, specialMultiply, div, factorial, \
    fib


class Test_without_array_1_1(TestCase):

    def test_swap(self):
        a0 = a = 10
        b0 = b = 20
        a, b = swap(a, b)
        self.assertEqual(a0, b, "a0 == b")
        self.assertEqual(b0, a, "b0 == a")

    def test_swap_numbers(self):
        a0 = a = 10
        b0 = b = 20
        a, b = swap_numbers(a, b)
        self.assertEqual(a0, b, "a0 == b")
        self.assertEqual(b0, a, "b0 == a")

    def test_pow_1(self):
        a = 3
        n = 4
        b = pow(a, n)
        self.assertEqual(b, 81, "pow({}, {}) = 81".format(a, n))

    def test_pow_2(self):
        a = 2
        n = 12
        expectedResult = 4096
        b = pow(a, n)
        self.assertEqual(b, expectedResult, "pow({}, {}) = {expectedResult}".format(a, n, expectedResult=expectedResult))

    def test_super_pow_1(self):
        a = 3
        n = 5
        expectedResult = 243
        b = super_pow(a, n)
        self.assertEqual(b, expectedResult, "super_pow({}, {}) = {}".format(a, n, expectedResult))

    def test_super_pow_2(self):
        a = 2
        n = 12
        expectedResult = 4096
        b = super_pow(a, n)
        self.assertEqual(b, expectedResult, "super_pow({}, {}) = {}".format(a, n, expectedResult))

    def test_super_pow_3(self):
        a = 2
        n = 0
        expectedResult = 1
        c = super_pow(a, n)
        self.assertEqual(c, expectedResult, "super_pow({}, {}) = {}".format(a, n, expectedResult))

    def test_multiply_1(self):
        a = 7
        b = 9
        expectedResult = 63
        c = multiply(a, b)
        self.assertEqual(c, expectedResult, "multiply({}, {}) = {}".format(a, b, expectedResult))

    def test_multiply_2(self):
        a = 0
        b = 9
        expectedResult = 0
        b = multiply(a, b)
        self.assertEqual(b, expectedResult, "multiply({}, {}) = {}".format(a, b, expectedResult))

    def test_specialMultiply_1(self):
        a = 7
        b = 9
        expectedResult = 63
        c = specialMultiply(a, b)
        self.assertEqual(c, expectedResult, "specialMultiply({}, {}) = {}".format(a, b, expectedResult))

    def test_specialMultiply_2(self):
        a = 0
        b = 9
        expectedResult = 0
        b = specialMultiply(a, b)
        self.assertEqual(b, expectedResult, "specialMultiply({}, {}) = {}".format(a, b, expectedResult))

    def test_div_1(self):
        a = 23
        d = 7
        expectedResult = (3, 2)
        result = div(a, d)
        self.assertEqual(result, expectedResult, "div({}, {}): div = {} mode = {}".format(a, d, *expectedResult))

    def test_div_2(self):
        a = 0
        d = 7
        expectedResult = (0, 0)
        result = div(a, d)
        self.assertEqual(result, expectedResult, "div({}, {}): div = {} mode = {}".format(a, d, *expectedResult))

    def test_div_3(self):
        a = 4
        d = 1
        expectedResult = (4, 0)
        result = div(a, d)
        self.assertEqual(result, expectedResult, "div({}, {}): div = {} mode = {}".format(a, d, *expectedResult))

    def test_div_4(self):
        a = 23
        d = 11
        expectedResult = (2, 1)
        result = div(a, d)
        self.assertEqual(result, expectedResult, "div({}, {}): div = {} mode = {}".format(a, d, *expectedResult))

    def test_factorial_1(self):
        n = 5
        expectedResult = 120
        result = factorial(n)
        self.assertEqual(result, expectedResult, "factorial({}) = {}".format(n, expectedResult))

    def test_factorial_2(self):
        n = 0
        expectedResult = 1
        result = factorial(n)
        self.assertEqual(result, expectedResult, "factorial({}) = {}".format(n, expectedResult))

    def test_fib_1(self):
        n = 10
        expectedResult = 55
        result = fib(n)
        self.assertEqual(result, expectedResult, "fib({}) = {}".format(n, expectedResult))

    def test_fib_2(self):
        n = 0
        expectedResult = 0
        result = fib(n)
        self.assertEqual(result, expectedResult, "fib({}) = {}".format(n, expectedResult))

    def test_fib_3(self):
        n = 1
        expectedResult = 1
        result = fib(n)
        self.assertEqual(result, expectedResult, "fib({}) = {}".format(n, expectedResult))

    def test_fib_4(self):
        n = 2
        expectedResult = 1
        result = fib(n)
        self.assertEqual(result, expectedResult, "fib({}) = {}".format(n, expectedResult))
