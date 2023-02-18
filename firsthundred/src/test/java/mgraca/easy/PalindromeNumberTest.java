package mgraca.easy;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class PalindromeNumberTest{
  @Test
  public void example1(){
    assertTrue(PalindromeNumber.isPalindrome(121) == true);
  }

  @Test
  public void example2(){
    assertTrue(PalindromeNumber.isPalindrome(-121) == false);
  }

  @Test
  public void example3(){
    assertTrue(PalindromeNumber.isPalindrome(10) == false);
  }

  @Test
  public void example4(){
    assertTrue(PalindromeNumber.isPalindrome(-101) == false);
  }

  @Test
  public void example5(){
    assertTrue(PalindromeNumber.isPalindrome(2000000009) == false);
  }

  @Test
  public void example6(){
    assertTrue(PalindromeNumber.isPalindrome(0) == true);
  }
}
