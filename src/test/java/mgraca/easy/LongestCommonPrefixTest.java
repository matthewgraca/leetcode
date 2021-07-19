package mgraca.easy;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class LongestCommonPrefixTest{
  @Test
  public void naiveExample1(){
    String[] input = new String[]{"flower", "flow", "flight"};
    String expectedOutput = "fl";
    String actualOutput = LongestCommonPrefix.naiveLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void naiveExample2(){
    String[] input = new String[]{"dog", "racecar", "car"};
    String expectedOutput = "";
    String actualOutput = LongestCommonPrefix.naiveLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void naiveExample3(){
    String[] input = new String[]{"", "", ""};
    String expectedOutput = "";
    String actualOutput = LongestCommonPrefix.naiveLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void naiveExample4(){
    String[] input = new String[]{"abc", "", ""};
    String expectedOutput = "";
    String actualOutput = LongestCommonPrefix.naiveLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void naiveExample5(){
    String[] input = new String[]{"hello"};
    String expectedOutput = "hello";
    String actualOutput = LongestCommonPrefix.naiveLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void fastExample1(){
    String[] input = new String[]{"flower", "flow", "flight"};
    String expectedOutput = "fl";
    String actualOutput = LongestCommonPrefix.fastLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void fastExample2(){
    String[] input = new String[]{"dog", "racecar", "car"};
    String expectedOutput = "";
    String actualOutput = LongestCommonPrefix.fastLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void fastExample3(){
    String[] input = new String[]{"", "", ""};
    String expectedOutput = "";
    String actualOutput = LongestCommonPrefix.fastLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void fastExample4(){
    String[] input = new String[]{"abc", "", ""};
    String expectedOutput = "";
    String actualOutput = LongestCommonPrefix.fastLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void fastExample5(){
    String[] input = new String[]{"hello"};
    String expectedOutput = "hello";
    String actualOutput = LongestCommonPrefix.fastLongestCommonPrefix(input);
    String errorMsg = "Expected \"" + expectedOutput + "\", returned \"" + actualOutput + "\"";
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

}
