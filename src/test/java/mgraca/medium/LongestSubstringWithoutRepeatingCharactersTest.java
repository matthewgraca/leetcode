package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class LongestSubstringWithoutRepeatingCharactersTest{
  /*
   * These test the queue-based implementation
   */
  @Test
  public void example1(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstring("abcabcbb") == 3);
  }

  @Test
  public void example2(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstring("bbbbb") == 1);
  }

  @Test
  public void example3(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstring("pwwkew") == 3);
  }

  @Test
  public void example4(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstring("") == 0);
  }

  @Test
  public void example5(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstring(" ") == 1);
  }

  @Test
  public void example6(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstring("dvdf") == 3);
  }
}
