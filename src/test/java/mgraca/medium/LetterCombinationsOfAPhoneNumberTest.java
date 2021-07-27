package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

import java.util.List;
import java.util.Arrays;

public class LetterCombinationsOfAPhoneNumberTest{
  @Test
  public void example1(){
    String input = "23";
    List<String> expectedOutput = Arrays.asList("ad","ae","af","bd","be","bf","cd","ce","cf");
    List<String> actualOutput = LetterCombinationsOfAPhoneNumber.letterCombinations(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput.equals(actualOutput));
  }

  @Test
  public void example2(){
    String input = "";
    List<String> expectedOutput = Arrays.asList();
    List<String> actualOutput = LetterCombinationsOfAPhoneNumber.letterCombinations(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput.equals(actualOutput));
  }

  @Test
  public void example3(){
    String input = "2";
    List<String> expectedOutput = Arrays.asList("a","b","c");
    List<String> actualOutput = LetterCombinationsOfAPhoneNumber.letterCombinations(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput.equals(actualOutput));
  }
}
