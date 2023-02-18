package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class IntegerToRomanTest{
  @Test
  public void example1(){
    int input = 3;
    String expectedOutput = "III";
    String actualOutput = IntegerToRoman.intToRoman(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example2(){
    int input = 4;
    String expectedOutput = "IV";
    String actualOutput = IntegerToRoman.intToRoman(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example3(){
    int input = 9;
    String expectedOutput = "IX";
    String actualOutput = IntegerToRoman.intToRoman(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example4(){
    int input = 58;
    String expectedOutput = "LVIII";
    String actualOutput = IntegerToRoman.intToRoman(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example5(){
    int input = 1994;
    String expectedOutput = "MCMXCIV";
    String actualOutput = IntegerToRoman.intToRoman(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example6(){
    int input = 300;
    String expectedOutput = "CCC";
    String actualOutput = IntegerToRoman.intToRoman(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example7(){
    int input = 3999;
    String expectedOutput = "MMMCMXCIX";
    String actualOutput = IntegerToRoman.intToRoman(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }
}
