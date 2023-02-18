package mgraca.easy;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class LongestCommonPrefixTest{
  @Test
  public void example1(){
    String[] input = new String[]{"flower", "flow", "flight"};
    String expectedOutput = "fl";
    String actualOutput = LongestCommonPrefix.longestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example2(){
    String[] input = new String[]{"dog", "racecar", "car"};
    String expectedOutput = "";
    String actualOutput = LongestCommonPrefix.longestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example3(){
    String[] input = new String[]{"", "", ""};
    String expectedOutput = "";
    String actualOutput = LongestCommonPrefix.longestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example4(){
    String[] input = new String[]{"abc", "", ""};
    String expectedOutput = "";
    String actualOutput = LongestCommonPrefix.longestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example5(){
    String[] input = new String[]{"hello"};
    String expectedOutput = "hello";
    String actualOutput = LongestCommonPrefix.longestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }
}
