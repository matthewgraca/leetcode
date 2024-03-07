package solutions.twopointers;

/*
 * https://leetcode.com/problems/valid-palindrome/
 *
 * Complexity
 *  Time: O(n)
 *    O(n) for lower case and replace all
 *    O(n) for scan
 *  Space: O(1)
 */
public class ValidPalindrome{
  public static boolean isPalindrome(String s){
    // force lower case, then remove non-alphanumeric characters
    s = s.toLowerCase().replaceAll("[^a-z0-9]", "");

    // check palindrome using a left-right scan
    char right, left;
    int n = s.length();
    for (int i = 0, j = n-1; i < n/2; i++, j--){
      if (s.charAt(i) != s.charAt(j))
        return false;
    }

    return true;
  }
}
