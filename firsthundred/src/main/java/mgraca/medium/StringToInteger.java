package mgraca.medium;

/*
 * Description: Implement the myAtoi(string s) function, which converts a string to a 32-bit 
 *  signed integer (similar to C/C++'s atoi function).
 *
 *  The algorithm for myAtoi(string s) is as follows:
 *  1. Read in and ignore any leading whitespace.
 *  2. Check if the next character (if not already at the end of the string) is '-' or '+'.
 *      Read this character in if it is either. This determines if the final result is negative or 
 *      positive respectively. Assume the result is positive if neither is present.
 *  3. Read in next the characters until the next non-digit charcter or the end of the input is 
 *      reached.
 *      The rest of the string is ignored.
 *  4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were 
 *      read, then the integer is 0. Change the sign as necessary (from step 2).
 *  5. If the integer is out of the 32-bit signed integer range [-2^(31), 2^(31) - 1], then clamp 
 *      the integer so that it remains in the range. Specifically, integers less than -2^(31) 
 *      should be clamped to -2^(31), and integers greater than 2^(31) - 1 should be clamped to 
 *      2^(31) - 1.
 *  6. Return the integer as the final result.
 *
 * Note:
 *  Only the space character ' ' is considered a whitespace character.
 *  Do not ignore any characters other than the leading whitespace or the rest of the string after 
 *    the digits.
 * 
 * Constraints:
 *  0 <= s.length <= 200
 *  s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
 *
 * Complexity:
 *  Time:   O(n)
 *  Space:  O(1) - Assumes the implementation of substring is O(1) space; else O(n) if it uses
 *                  some auxillary container when creating the substring
 */
public class StringToInteger{
  public static int myAtoi(String s){
    int solution = 0;
    s = s.trim();
    if (s.isEmpty()){
      solution = 0;
    }
    else{
      // check if the leading character is +/-
      boolean positive = true;
      int start = 0;
      char leadingChar = s.charAt(start);
      if (leadingChar == '-'){
        positive = false;
        start++;
      }
      else if (leadingChar == '+'){
        start++;
      }
      else{
        // do nothing
      }

      // search through string, end if a letter is found/reached end
      int i = start;
      boolean letterFound = false;
      while (i < s.length() && !letterFound){
        if (Character.isDigit(s.charAt(i))){
          i++;
        }
        else{
          letterFound = true;
        }
      }
      s = s.substring(start, i);  // s contains the int, may have leading 0s

      // remove leading 0s
      i = 0;
      boolean removedLeadingZeroes = false;
      while (i < s.length() && !removedLeadingZeroes){
        if (s.charAt(i) == '0'){
          i++;
        }
        else{
          removedLeadingZeroes = true;
        }
      }
      s = s.substring(i, s.length());

      // if the string is exhausted and empty, return 0
      if (s.isEmpty()){
        solution = 0;
      }

      // here, we have a string of ints. convert string to integer
      boolean flowDetected = false;
      for (int j = 0; j < s.length() && !flowDetected; j++){
        // detect over/underflow
        if (solution * 10 / 10 != solution                          || 
            (solution * 10 == 2147483640 && s.charAt(j) - 48 > 7)   || 
            (solution * 10 == -2147483640 && s.charAt(j) - 48 > 8)  ){
          flowDetected = true;
          if (!positive){
            solution = Integer.MIN_VALUE;
          }
          else{
            solution = Integer.MAX_VALUE;
          }
        }
        // properly append the int solution
        else{
          solution *= 10;
          if (!positive){
            solution -= s.charAt(j) - 48;
          }
          else{
            solution += s.charAt(j) - 48;
          }
        }
      }
    }
    return solution;
  }
}
