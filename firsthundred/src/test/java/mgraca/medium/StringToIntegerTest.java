package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class StringToIntegerTest{
  @Test
  public void example1(){
    int expectedOutput = 42;
    int output = StringToInteger.myAtoi("42");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example2(){
    int expectedOutput = -42;
    int output = StringToInteger.myAtoi("   -42");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example3(){
    int expectedOutput = 4193;
    int output = StringToInteger.myAtoi("4193 with words");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example4(){
    int expectedOutput = 0;
    int output = StringToInteger.myAtoi("words and 987");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example5(){
    int expectedOutput = -2147483648;
    int output = StringToInteger.myAtoi("-91283472332");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example6(){
    int expectedOutput = 72;
    int output = StringToInteger.myAtoi("+72");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example7(){
    int expectedOutput = 0;
    int output = StringToInteger.myAtoi("            ");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example8(){
    int expectedOutput = 0;
    int output = StringToInteger.myAtoi("+");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example9(){
    int expectedOutput = 62;
    int output = StringToInteger.myAtoi("+00000062abc");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example10(){
    int expectedOutput = 2147483647;
    int output = StringToInteger.myAtoi("91283472332");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example11(){
    int expectedOutput = 2147483647;
    int output = StringToInteger.myAtoi("2147483648");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example12(){
    int expectedOutput = -2147483648;
    int output = StringToInteger.myAtoi("-2147483649");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }

  @Test
  public void example13(){
    int expectedOutput = 2147483646;
    int output = StringToInteger.myAtoi("2147483646");
    String errorMsg = "Expected " + expectedOutput + ", got " + output;
    assertTrue(errorMsg, output == expectedOutput);
  }
}
