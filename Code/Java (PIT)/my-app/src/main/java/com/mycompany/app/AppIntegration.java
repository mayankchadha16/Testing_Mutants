package com.mycompany.app;

class UtilityMethodsIntegration {

    // Utility method to return
    // sum of square of digit of n
    public int numSquareSum(int n) {
        int squareSum = 0;

        while (n != 0) {
            squareSum += (n % 10) * (n % 10);
            n /= 10;
        }

        return squareSum;
    }

    public int power(int x, int y) {
        if (y == 0) {
            return 1;
        }
        if (y % 2 == 0) {
            int temp = power(x, y / 2);
            return temp * temp;
        }

        int temp = power(x, y / 2);
        return x * temp * temp;
    }

    // Function to calculate number of digits in the number
    public int order(int x) {
        int n = 0;

        while (x != 0) {
            n = n + 1;
            x = x / 10;
        }

        // ###############################################################
        // # Original
        // # return n
        return n + 1;
        // # Integration Return Expression Modification (IREM): Each
        // # expression in each return statement in a method is modified
        // # by applying the UOI (Unary Operator Insertion)
        // ###############################################################
    }

}

public class AppIntegration {
    static UtilityMethodsIntegration util = new UtilityMethodsIntegration();

    // A number is called happy if it leads to 1 after a sequence of steps wherein
    // each step number
    // is replaced by the sum of squares of its digit that is if
    // we start with Happy Number and keep replacing it with digits square sum, we
    // reach 1.
    public static boolean isHappynumber(int num) {
        int slow = num;
        int fast = num;

        // Heavily Integration Testing as
        // it calls numSquareSum
        while (true) {
            // ###############################################################
            // # original
            // # slow = util.numSquareSum(slow)
            slow = util.numSquareSum(fast);
            // # Integration Parameter Variable Replacement (IVPR): Each
            // # parameter in a method call is replaced by each other variable
            // # of compatible type in the scope of the method call.
            // ###############################################################
            fast = util.numSquareSum(util.numSquareSum(fast));

            if (slow != fast) {
                continue;
            } else {
                break;
            }
        }

        if (slow == 1) {
            return true;
        } else {
            return false;
        }
    }

    // Given a number x, determine whether the given number is Armstrong number or
    // not.
    // # A positive integer of n digits is called an Armstrong number of order n
    // (order is number of digits) if.
    // # abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
    public static boolean isArmstrong(int num) {

        // Heavily integration testing
        // calls power as well as order
        // ################################################################
        // int digitCount = util.order(num);
        // # original
        int digitCount = 1;
        // # Integration Method Call Deletion (IMCD): Each method call
        // # is deleted. If the method returns a value and it is used in an
        // # expression, the method call is replaced with an appropriate
        // # constant value
        // ################################################################

        int temp = num;
        int sumOfPowers = 0;

        while (temp != 0) {
            int digit = temp % 10;
            // ################################################################
            // # original
            // sumOfPowers += util.power(digit, digitCount);
            sumOfPowers += util.power(digitCount, digit);
            // # Integration Parameter Exchange (IPEX): Each parameter in a
            // # method call is exchanged with each parameter of compatible
            // # type in that method call.
            // ################################################################
            temp /= 10;
        }

        if (sumOfPowers == num) {
            return true;
        } else {
            return false;
        }
    }

    // Narcissistic Number is a number that is the sum of its own digits each raised
    // to the power of the number of digits
    public static boolean isNarcissistic(int num) {
        int numDigits = util.order(num);
        int originalNum = num;
        int totalSum = 0;

        while (originalNum != 0) {
            totalSum = totalSum + util.power(originalNum % 10, numDigits);
            originalNum = originalNum / 10;
        }

        if (num == totalSum) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
    }
}
