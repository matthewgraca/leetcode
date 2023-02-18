package mgraca.easy;

/*
 * Description: Given an integer x, return true if x is palindrome integer.
 *  An integer is a palindrome when it reads the same backward as forward. 
 *  For example, 121 is palindrome while 123 is not.
 *
 * Try solving it without converting x into a string!
 *
 * Constraints:
 *  -2^(31) <= x <= 2^(31) - 1
 *
 * Complexity:
 *  Time:   O(n)
 *  Space:  O(1)
 */
public class PalindromeNumber{
  public static boolean isPalindrome(int x){
    boolean isPalindrome;
    if (x < 0){
      isPalindrome = false;
    }
    else{
      int temp = x;
      int reverse = 0;
      // build a reversed x
      while (temp > 0){
        reverse *= 10;
        reverse += temp % 10;
        temp /= 10;
      }
      // check if the reversed x is the same as x
      if (reverse == x){
        isPalindrome = true;
      }
      else{
        isPalindrome = false;
      }
    }
    return isPalindrome;
  }
}
