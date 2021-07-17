package mgraca.easy;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class RomanToIntegerTest{
  @Test
  public void example1(){
    String input = "III";
    int expectedOutput = 3;
    int actualOutput = RomanToInteger.romanToInt(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput);
  }

  @Test
  public void example2(){
    String input = "IV";
    int expectedOutput = 4;
    int actualOutput = RomanToInteger.romanToInt(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput);
  }

  @Test
  public void example3(){
    String input = "IX";
    int expectedOutput = 9;
    int actualOutput = RomanToInteger.romanToInt(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput);
  }

  @Test
  public void example4(){
    String input = "LVIII";
    int expectedOutput = 58;
    int actualOutput = RomanToInteger.romanToInt(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput);
  }

  @Test
  public void example5(){
    String input = "MCMXCIV";
    int expectedOutput = 1994;
    int actualOutput = RomanToInteger.romanToInt(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput);
  }
}
