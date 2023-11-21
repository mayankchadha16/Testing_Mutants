from utilityMethodsIntegration import *


# A number is called happy if it leads to 1 after a sequence of steps wherein each step number
# is replaced by the sum of squares of its digit that is if
# # we start with Happy Number and keep replacing it with digits square sum, we reach 1.
def isHappynumber(num):

    slow = num
    fast = num

    # Heavily Integration Testing as
    # it calls numSquareSum
    while (True):

        ###############################################################
        # original
        # slow = numSquareSum(slow)
        slow = numSquareSum(fast)
        # Integration Parameter Variable Replacement (IVPR): Each
        # parameter in a method call is replaced by each other variable
        # of compatible type in the scope of the method call.
        ###############################################################

        fast = numSquareSum(numSquareSum(fast))

        if (slow != fast):
            continue

        else:
            break

    if (slow == 1):
        return True

    else:
        return False


# Given a number x, determine whether the given number is Armstrong number or not.
#  A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
def isArmstrong(num):

    # Heavily integration testing
    # calls power as well as order
    ################################################################
    # original
    # digit_count = order(num)
    digit_count = 1
    # Integration Method Call Deletion (IMCD): Each method call
    # is deleted. If the method returns a value and it is used in an
    # expression, the method call is replaced with an appropriate
    # constant value
    ################################################################

    temp = num
    sum_of_powers = 0

    while temp != 0:
        digit = temp % 10
        ################################################################
        # original
        # sum_of_powers += power(digit, digit_count)
        sum_of_powers += power(digit_count, digit)
        # Integration Parameter Exchange (IPEX): Each parameter in a
        # method call is exchanged with each parameter of compatible
        # type in that method call.
        ################################################################
        temp //= 10

    if (sum_of_powers == num):
        return True

    else:
        return False

# Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits
def isNarcissistic(num):

    num_digits = order(num)
    original_num = num
    total_sum = 0

    while (original_num):
        total_sum = total_sum + power(original_num % 10, num_digits)
        original_num = original_num // 10

    if (num == total_sum):
        return True

    else:
        return False