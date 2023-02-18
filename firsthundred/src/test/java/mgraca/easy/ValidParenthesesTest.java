package mgraca.easy;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ValidParenthesesTest{
  @Test
  public void example1(){
    String input = "()";
    boolean expected = true;
    boolean actual = ValidParentheses.isValid(input);
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual == expected);
  }

  @Test
  public void example2(){
    String input = "()[]{}";
    boolean expected = true;
    boolean actual = ValidParentheses.isValid(input);
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual == expected);
  }

  @Test
  public void example3(){
    String input = "(]";
    boolean expected = false;
    boolean actual = ValidParentheses.isValid(input);
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual == expected);
  }

  @Test
  public void example4(){
    String input = "{[]}";
    boolean expected = true;
    boolean actual = ValidParentheses.isValid(input);
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual == expected);
  }
}
