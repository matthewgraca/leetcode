package mgraca;

import static org.junit.Assert.*;
import org.junit.Test;

import java.util.List;
import java.util.Arrays;
import java.util.HashSet;

public class GenerateParenthesesTest{
  @Test
  public void example1(){
    List<String> expected = Arrays.asList("((()))", "(()())", "(())()", "()(())", "()()()");
    List<String> actual = GenerateParentheses.generateParenthesis(3);
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual.containsAll(expected) && expected.containsAll(actual));
  }

  @Test
  public void example2(){
    List<String> expected = Arrays.asList("()");
    List<String> actual = GenerateParentheses.generateParenthesis(1);
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual.containsAll(expected) && expected.containsAll(actual));
  }

  @Test
  public void example3(){
    List<String> expected = Arrays.asList("(((())))","((()()))","((())())",
                                          "((()))()","(()(()))","(()()())",
                                          "(()())()","(())(())","(())()()",
                                          "()((()))","()(()())","()(())()",
                                          "()()(())","()()()()");
    List<String> actual = GenerateParentheses.generateParenthesis(4);
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual.containsAll(expected) && expected.containsAll(actual));
  }
}
