package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class LongestPalindromicSubstringTest{
  @Test
  public void example1(){
    String s = LongestPalindromicSubstring.longestPalindrome("babad");
    assertTrue(s.equals("bab") || s.equals("aba"));
  }

  @Test
  public void example2(){
    String s = LongestPalindromicSubstring.longestPalindrome("cbbd");
    assertTrue(s.equals("bb"));
  }

  @Test
  public void example3(){
    String s = LongestPalindromicSubstring.longestPalindrome("a");
    assertTrue(s.equals("a"));
  }

  @Test
  public void example4(){
    String s = LongestPalindromicSubstring.longestPalindrome("ac");
    assertTrue(s.equals("a"));
  }

  @Test
  public void example5(){
    String s = LongestPalindromicSubstring.longestPalindrome("bb");
    assertTrue(s.equals("bb"));
  }
}
