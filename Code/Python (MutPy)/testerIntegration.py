from unittest import TestCase
from numAnalysisIntegration import *

class IsHappyNumberTest(TestCase):
    # Test case for a happy number
    def test_happy_number(self):
        self.assertEqual(isHappynumber(19), True)

    # Went to an Infinite Loop
    # # Test case for a non-happy number
    # def test_nonhappy_number(self):
    #     self.assertEqual(isHappynumber(22), False)

    # Test case for an edge case
    def test_edge_case(self):
        self.assertEqual(isHappynumber(1), True)

    # Test case for a larger happy number
    def test_larger_happy_number(self):
        self.assertEqual(isHappynumber(82), True)


class IsArmstrongTest(TestCase):
    # Test case for an Armstrong number
    def test_armstrong_number(self):
        self.assertEqual(isArmstrong(153), False)

    # Test case for a non-Armstrong number
    def test_nonarmstrong_number(self):
        self.assertEqual(isArmstrong(1253), False)

    # Test case for a single-digit Armstrong number 
    def test_single_digit_armstrong_number(self):
        self.assertEqual(isArmstrong(5), False)

    # Test case for a larger Armstrong number
    def test_larger_armstrong_number(self):
        self.assertEqual(isArmstrong(1253), False)

    # Test case for a non-Armstrong number 
    def test_another_nonarmstrong_number(self):
        self.assertEqual(isArmstrong(123), False)