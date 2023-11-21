package com.mycompany.app;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class AppTestIntegration {
    // Happy Number
    // #######################################################################################################################//
    @Test
    public void test_happy_number() {
        assertEquals(AppIntegration.isHappynumber(19), true);
    }

    // Armstrong Numbers
    // #######################################################################################################################//
    @Test
    public void test_armstrong_number() {
        assertEquals(AppIntegration.isArmstrong(153), false);
    }

    @Test
    public void test_nonarmstrong_number() {
        assertEquals(AppIntegration.isArmstrong(1253), false);
    }

    @Test
    public void test_single_digit_armstrong_number() {
        assertEquals(AppIntegration.isArmstrong(5), false);
    }

    // Narcissistic Numbers
    // #######################################################################################################################//
    @Test
    public void test_narcissistic_number() {
        assertEquals(AppIntegration.isNarcissistic(153), false);
    }

    @Test
    public void test_nonnarcissistic_number() {
        assertEquals(AppIntegration.isNarcissistic(129), false);
    }

    @Test
    public void test_smallest_narcissistic_number() {
        assertEquals(AppIntegration.isNarcissistic(0), true);
    }

    @Test
    public void test_larger_narcissistic_number() {
        assertEquals(AppIntegration.isNarcissistic(9474), false);
    }
}
