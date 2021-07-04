package mgraca.medium;

/*
 * Description: Given a string s, return the longest palindromic substring in s.
 *
 * Constraints:
 *  1 <= s.length <= 1000
 *  s consist of only digits and English letters (lower-case and/or upper-case)
 *
 * Complexity:
 *  Time:   O(n^2)
 *  Space:  O(n) 
 */
public class LongestPalindromicSubstring{
  public static String longestPalindrome(String s){
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++){
      char comparingChar = s.charAt(i);
      int left = i;
      int right = i;

      // scan and include duplicate characters from the left
      while (left >= 0 && s.charAt(left) == comparingChar){
        left--;
      }

      // scan and include duplicate characters from the right
      while (right < s.length() && s.charAt(right) == comparingChar){
        right++;
      }

      // scan and include matching characters from the right and left to add to the palindrome
      boolean palindromeFound = true;
      while (left >= 0 && right < s.length() && palindromeFound){
        if (s.charAt(right) != s.charAt(left)){
          palindromeFound = false;
        }
        else{
          left--;
          right++;
        }
      }

      // determine if the palindrome found is the longest one yet
      // note: left + 1 and right - 1 are the proper true indeces... 
      //  ...but right doesn't get decremented b/c of s.substring()'s behavior
      left++;
      if (end - start < right - left){
        start = left;
        end = right;
      }
    }
    return s.substring(start, end);
  }
}
