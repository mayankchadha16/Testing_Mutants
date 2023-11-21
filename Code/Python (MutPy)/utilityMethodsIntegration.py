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

    ###############################################################
    # Original
    # return n
    return n + 1
    # Integration Return Expression Modification (IREM): Each
    # expression in each return statement in a method is modified
    # by applying the UOI (Unary Operator Insertion)
    ###############################################################
