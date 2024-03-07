package solutions.twopointers;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import static solutions.twopointers.ValidPalindrome.isPalindrome;

public class ValidPalindromeTest{
  @Test
  public void example1(){
    String input = "A man, a plan, a canal: Panama";
    boolean expected = true;
    boolean actual = isPalindrome(input);

    assertTrue(expected == actual);
  }

  @Test
  public void example2(){
    String input = "race a car";
    boolean expected = false;
    boolean actual = isPalindrome(input);

    assertTrue(expected == actual);
  }

  @Test
  public void example3(){
    String input = " ";
    boolean expected = true;
    boolean actual = isPalindrome(input);

    assertTrue(expected == actual);
  }
}
