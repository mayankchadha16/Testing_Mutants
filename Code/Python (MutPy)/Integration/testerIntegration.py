from unittest import TestCase
from numAnalysisIntegration import *


class IsHappyNumberTest(TestCase):
    # Test case for a happy number
    def test_happy_number(self):
        # Mutant Survived initially it was true only
        self.assertEqual(isHappynumber(19), True)

    # Went to an Infinite Loop: TimeOut
    # # Test case for a non-happy number
    # def test_nonhappy_number(self):
    #     self.assertEqual(isHappynumber(22), False)


class IsArmstrongTest(TestCase):
    # Test case for an Armstrong number
    def test_armstrong_number(self):
        # Mutant Killed initially it was true
        self.assertEqual(isArmstrong(153), False)

    # Test case for a non-Armstrong number
    def test_nonarmstrong_number(self):
        # Mutant Survived initially it was false only
        self.assertEqual(isArmstrong(1253), False)

    # Test case for a single-digit Armstrong number
    def test_single_digit_armstrong_number(self):
        # Mutant Killed initially it was true
        self.assertEqual(isArmstrong(5), False)


class IsNarcissisticTest(TestCase):
    # Test case for a narcissistic number
    def test_narcissistic_number(self):
        # Mutant Killed initially it was true
        self.assertEqual(isNarcissistic(153), False)

    # Test case for a non-narcissistic number
    def test_nonnarcissistic_number(self):
        # Mutant Survived initially it was false only
        self.assertEqual(isNarcissistic(129), False)

    # Test case for the smallest narcissistic number
    def test_smallest_narcissistic_number(self):
        # Mutant Survived initially it was true only
        self.assertEqual(isNarcissistic(0), True)

    # Test case for a larger narcissistic number
    def test_larger_narcissistic_number(self):
        # Mutant Killed initially it was true
        self.assertEqual(isNarcissistic(9474), False)
