from math import log

# Utility method to check
# for number being odd or even
def isEven(num):
    return num % 2 == 0
def isOdd(num):
    return num % 2 == 1


# Utility method to return
# sum of square of digit of n
def numSquareSum(n):
    squareSum = 0

    while (n):
        squareSum += (n % 10) * (n % 10)
        n = int(n / 10)

    return squareSum


# Function to calculate x raised to
# the power y
def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)

    return x * power(x, y // 2) * power(x, y // 2)


# Function to calculate number of digits in the number
def order(x):
    n = 0

    while (x != 0):
        n = n + 1
        x = x // 10

    return n


# Utility method to calculate sqrt of a number
def custom_sqrt(x):

    if x == 0 or x == 1:
        return x

    guess = x / 2.0

    while True:
        new_guess = 0.5 * (guess + x / guess)

        if abs(new_guess - guess) < 1e-10:
            return new_guess

        guess = new_guess


# Utility function to check if
# number is a perfect power or not
def isPower(a):
    if (a == 1):
        return True

    for i in range(2, a, 1):
        val = log(a) / log(i)
        if ((val - int(val)) < 0.00000001):
            return True

    return False
