package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class LongestSubstringWithoutRepeatingCharactersTest{
  /*
   * These test the queue-based implementation
   */
  @Test
  public void example1Queue(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringQueue("abcabcbb") == 3);
  }

  @Test
  public void example2Queue(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringQueue("bbbbb") == 1);
  }

  @Test
  public void example3Queue(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringQueue("pwwkew") == 3);
  }

  @Test
  public void example4Queue(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringQueue("") == 0);
  }

  @Test
  public void example5Queue(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringQueue(" ") == 1);
  }

  @Test
  public void example6Queue(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringQueue("dvdf") == 3);
  }

  /*
   * These test the sliding window implementation
   */
  @Test
  public void example1SlidingWindow(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringSlidingWindow("abcabcbb") == 3);
  }

  @Test
  public void example2SlidingWindow(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringSlidingWindow("bbbbb") == 1);
  }

  @Test
  public void example3SlidingWindow(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringSlidingWindow("pwwkew") == 3);
  }

  @Test
  public void example4SlidingWindow(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringSlidingWindow("") == 0);
  }

  @Test
  public void example5SlidingWindow(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringSlidingWindow(" ") == 1);
  }

  @Test
  public void example6SlidingWindow(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringSlidingWindow("dvdf") == 3);
  }

  @Test
  public void example7SlidingWindow(){
    assertTrue(LongestSubstringWithoutRepeatingCharacters.
        lengthOfLongestSubstringSlidingWindow("abba") == 2);
  }
}
