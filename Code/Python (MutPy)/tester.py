from unittest import TestCase
from numAnalysis import *


class IsPrimeTest(TestCase):
    # test case to check for 2
    def test_smallprime(self):
        self.assertEqual(isPrime(2), True)

    # test case for checking non prime nums
    def test_nonprime(self):
        self.assertEqual(isPrime(12), False)

    # test case to check prime nums
    def test_prime(self):
        self.assertEqual(isPrime(19), True)

    # test case to check invalid input
    def test_invalid(self):
        self.assertEqual(isPrime(-1), False)


class IsPerfectTest(TestCase):
    # Test case to check for a perfect number
    def test_perfect_number(self):
        self.assertEqual(isPerfect(28), True)

    # Test case for checking a non-perfect number
    def test_nonperfect_number(self):
        self.assertEqual(isPerfect(12), False)

    # Test case to check an edge case
    def test_edge_case(self):
        self.assertEqual(isPerfect(1), False)

    # Test case to check for another perfect number
    def test_another_perfect_number(self):
        self.assertEqual(isPerfect(496), True)


class IsHarshadTest(TestCase):
    # Test case for a Harshad number
    def test_harshad_number(self):
        self.assertEqual(isHarshad(18), True)

    # Test case for a non-Harshad number
    def test_nonharshad_number(self):
        self.assertEqual(isHarshad(23), False)

    # Test case for an edge case
    def test_edge_case(self):
        self.assertEqual(isHarshad(0), False)

    # Test case for a larger Harshad number
    def test_larger_harshad_number(self):
        self.assertEqual(isHarshad(27), True)


class IsHappyNumberTest(TestCase):
    # Test case for a happy number
    def test_happy_number(self):
        self.assertEqual(isHappynumber(19), True)

    # Test case for a non-happy number
    def test_nonhappy_number(self):
        self.assertEqual(isHappynumber(22), False)

    # Test case for an edge case
    def test_edge_case(self):
        self.assertEqual(isHappynumber(1), True)

    # Test case for a larger happy number
    def test_larger_happy_number(self):
        self.assertEqual(isHappynumber(82), True)


class IsTriangularTest(TestCase):
    # Test case for a triangular number
    def test_triangular_number_0(self):
        self.assertEqual(isTriangular(0), True)

    # Test case for a non-triangular number
    def test_nontriangular_number(self):
        self.assertEqual(isTriangular(5), False)

    # Test case for a larger triangular number
    def test_larger_triangular_number(self):
        self.assertEqual(isTriangular(10), True)

    # Test case for a non-triangular number
    def test_another_nontriangular_number(self):
        self.assertEqual(isTriangular(696), False)


class IsPalindromeTest(TestCase):
    # Test case for a non-palindrome number
    def test_nonpalindrome_number(self):
        self.assertEqual(isPalindrome(456), False)

    # Test case for a single-digit number
    def test_single_digit_number(self):
        self.assertEqual(isPalindrome(7), True)

    # Test case for a palindrome number
    def test_larger_palindrome_number(self):
        self.assertEqual(isPalindrome(1221), True)

    # Test case for a non-palindrome number
    def test_another_nonpalindrome_number(self):
        self.assertEqual(isPalindrome(12345), False)


class IsArmstrongTest(TestCase):
    # Test case for an Armstrong number
    def test_armstrong_number(self):
        self.assertEqual(isArmstrong(153), True)

    # Test case for a non-Armstrong number
    def test_nonarmstrong_number(self):
        self.assertEqual(isArmstrong(1253), False)

    # Test case for a single-digit Armstrong number (5)
    def test_single_digit_armstrong_number(self):
        self.assertEqual(isArmstrong(5), True)

    # Test case for a larger Armstrong number (1634)
    def test_larger_armstrong_number(self):
        self.assertEqual(isArmstrong(1634), True)

    # Test case for a non-Armstrong number (123)
    def test_another_nonarmstrong_number(self):
        self.assertEqual(isArmstrong(123), False)


class IsPerfectSquareTest(TestCase):
    # Test case for a perfect square
    def test_perfect_square(self):
        self.assertEqual(isPerfectSquare(16), True)

    # Test case for a non-perfect square
    def test_nonperfect_square(self):
        self.assertEqual(isPerfectSquare(10), False)

    # Test case for the smallest perfect square
    def test_smallest_perfect_square(self):
        self.assertEqual(isPerfectSquare(1), True)

    # Test case for a larger perfect square
    def test_larger_perfect_square(self):
        self.assertEqual(isPerfectSquare(81), True)


class IsSquareFreeTest(TestCase):
    # Test case for a square-free number
    def test_square_free_number(self):
        self.assertEqual(isSquareFree(17), True)

    # Test case for a non-square-free number
    def test_nonsquare_free_number(self):
        self.assertEqual(isSquareFree(16), False)

    # Test case for a larger square-free number
    def test_larger_square_free_number(self):
        self.assertEqual(isSquareFree(19), True)

    # Test case for the smallest square-free number
    def test_smallest_square_free_number(self):
        self.assertEqual(isSquareFree(1), True)


class IsNarcissisticTest(TestCase):
    # Test case for a narcissistic number
    def test_narcissistic_number(self):
        self.assertEqual(isNarcissistic(153), True)

    # Test case for a non-narcissistic number
    def test_nonnarcissistic_number(self):
        self.assertEqual(isNarcissistic(129), False)

    # Test case for the smallest narcissistic number
    def test_smallest_narcissistic_number(self):
        self.assertEqual(isNarcissistic(0), True)

    # Test case for a larger narcissistic number
    def test_larger_narcissistic_number(self):
        self.assertEqual(isNarcissistic(9474), True)


class IsPowerfulTest(TestCase):
    # Test case for a powerful number (16)
    def test_powerful_number(self):
        self.assertEqual(isPowerful(16), True)

    # Test case for a non-powerful number (12)
    def test_nonpowerful_number(self):
        self.assertEqual(isPowerful(12), False)

    # Test case for the smallest powerful number (1)
    def test_smallest_powerful_number(self):
        self.assertEqual(isPowerful(1), True)

    # Test case for a non-powerful number (30)
    def test_another_nonpowerful_number(self):
        self.assertEqual(isPowerful(30), False)


class IsAchillesNumberTest(TestCase):
    # Test case for an Achilles number (72)
    def test_achilles_number(self):
        self.assertEqual(isAchillesNumber(72), True)

    # Test case for a non-Achilles number (16)
    def test_nonachilles_number(self):
        self.assertEqual(isAchillesNumber(16), False)

    # Test case for another Achilles number (180)
    def test_another_achilles_number(self):
        self.assertEqual(isAchillesNumber(392), True)

    # Test case for a non-Achilles number (25)
    def test_another_nonachilles_number(self):
        self.assertEqual(isAchillesNumber(25), False)

class IsStirlingTest(TestCase):
    # Test case for a valid input (n=5, k=2)
    def test_valid_input(self):
        self.assertEqual(isStirling(5, 2), 15)

    # Test case for n <= 0 (n=-1, k=2)
    def test_negative_n(self):
        self.assertEqual(isStirling(-1, 2), 1)

    # Test case for n != 0 and n == k (n=3, k=3)
    def test_n_equals_k(self):
        self.assertEqual(isStirling(3, 3), 1)

    # Test case for n < k (n=2, k=5)
    def test_n_less_than_k(self):
        self.assertEqual(isStirling(2, 5), 0)


class IsEulerianTest(TestCase):
    # Test case 1
    def test_case1(self):
        self.assertEqual(isEulerian(3, 1), 4)

    # Test case 2
    def test_case2(self):
        self.assertEqual(isEulerian(4, 1), 11)