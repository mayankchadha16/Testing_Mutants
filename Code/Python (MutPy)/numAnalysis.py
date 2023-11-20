from utilityMethods import *


# A prime number is defined as a natural number greater than 1 and is divisible by only 1 and itself.
def isPrime(num):

    if isEven(num) and num != 2:
        return False

    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                return False

        else:
            return True

    else:
        return False


# A perfect number is a positive integer that is equal to the sum of its proper divisors.
def isPerfect(num):
    sum_divisors = 0

    for i in range(1, num):

        if num % i == 0:
            sum_divisors += i

    if (sum_divisors == num):
        return True

    else:
        return False


# If a number is divisible by the sum of its digits, then it will be known as a Harshad Number.
def isHarshad(num):

    if (num == 0):
        return False

    remainder = total_sum = 0

    original_num = num

    while num > 0:
        remainder = num % 10
        total_sum += remainder
        num //= 10

    if (original_num % total_sum == 0):
        return True

    else:
        return False


# A number is called happy if it leads to 1 after a sequence of steps wherein each step number
# is replaced by the sum of squares of its digit that is if
# # we start with Happy Number and keep replacing it with digits square sum, we reach 1.
def isHappynumber(num):

    slow = num
    fast = num

    # Heavily Integration Testing as
    # it calls numSquareSum
    while (True):

        slow = numSquareSum(slow)

        fast = numSquareSum(numSquareSum(fast))

        if (slow != fast):
            continue

        else:
            break

    if (slow == 1):
        return True

    else:
        return False


# Triangular Numbers are those numbers which are obtained by continued summation of the natural numbers 1, 2, 3, 4, 5,...
def isTriangular(num):

    if num == 0 or num == 1:
        return True

    triangular_sum = 0

    for i in range(num):
        triangular_sum += i

        if triangular_sum == num:
            return True

        if i == num:
            return False

    return False


# A palindrome is nothing but any number or a string which remains unaltered when reversed.
def isPalindrome(num):

    original_num = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    if (original_num == reversed_num):
        return True

    else:
        return False


# Given a number x, determine whether the given number is Armstrong number or not.
#  A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
def isArmstrong(num):

    # Heavily integration testing
    # calls power as well as order
    digit_count = order(num)

    temp = num
    sum_of_powers = 0

    while temp != 0:
        digit = temp % 10
        sum_of_powers += power(digit, digit_count)
        temp //= 10

    if (sum_of_powers == num):
        return True

    else:
        return False


# Given a number n, check if it is a perfect square or not.
def isPerfectSquare(num):

    if num <= 1:
        return True

    left, right = 1, num

    while left <= right:

        mid = left + (right - left) // 2

        square = mid * mid

        if square == num:
            return True

        elif square < num:
            left = mid + 1

        else:
            right = mid - 1

    return False


# Returns true if n is
# a square free number,
# else returns false.
def isSquareFree(num):

    if num % 2 == 0:
        num = num / 2

    if num % 2 == 0:
        return False

    # Function for Integration Testing, since
    # it calls custom_sqrt
    for i in range(3, int(custom_sqrt(num) + 1)):

        if num % i == 0:
            num = num / i

        if num % i == 0:
            return False

    return True

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


# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it
def isPowerful(n):

    while (n % 2 == 0):
        power = 0
        while (n % 2 == 0):
            n /= 2
            power += 1

        if (power == 1):
            return False

    p = int(custom_sqrt(n)) + 1
    for factor in range(3, p, 2):

        power = 0
        while (n % factor == 0):
            n = n / factor
            power += 1

        if (power == 1):
            return False

    if (n == 1):
        return True

    else:
        return False


# An Achilles number is a number that is powerful
# but not a perfect power
def isAchillesNumber(n):

    # Integration Testing as it uses isPowerful and PerfectSquare
    if (isPowerful(n) == True and
            isPower(n) == False):
        return True

    else:
        return False


# Stirling Number of the second kind, S(n, k), is the number of ways of splitting “n” items in “k” non-empty sets.
# The formula used for calculating Stirling Number is:
# S(n, k) = k* S(n-1, k) + S(n-1, k-1)
def isStirling(n, k):

    original_n = n
    original_k = k

    if n <= 0:
        return 1

    elif k <= 0:
        return 0

    elif n == 0 and k == 0:
        return -1

    elif n != 0 and n == k:
        return 1

    elif n < k:
        return 0

    else:
        recursive_result_1 = isStirling(original_n - 1, original_k)
        temp_result = original_k * recursive_result_1
        return (original_k * isStirling(original_n - 1, original_k)) + isStirling(original_n - 1, original_k - 1)


# the Eulerian Number A(n, m),
# is the number of permutations of the numbers 1 to n in which exactly m elements are greater than previous element.
def isEulerian(n, m):
    
    if (m >= n or n == 0):
        return 0

    if (m == 0):
        return 1

    return ((n - m) * isEulerian(n - 1, m - 1) +
            (m + 1) * isEulerian(n - 1, m))
