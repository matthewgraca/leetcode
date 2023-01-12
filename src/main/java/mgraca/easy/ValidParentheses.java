package mgraca.easy;

import java.util.Stack;
/*
 * Description: Given a string `s` containing just the characters '(', ')', 
 *  '[', ']', '{', '}', determine if the input string is valid.
 *  An input string is valid if:
 *    - Open brackets must be closed by the same type of brackets
 *    - Open brackets must be closed in the correct order
 *    - Every close bracket has a corresponding open bracket of the same type
 * 
 * Constraints:
 *  1 <= s.length <= 10^4
 *  s consists of parentheses only
 * 
 * Complexity:
 *  Time:   O(n), where n is the size of the input string. We increment 
 *    through the entire string to check for pairs.
 *  Space:  O(n), where n is the size of the input string. Worst case, the 
 *    entire string is made of zero pairs, which we have to increment through, 
 *    requiring a stack of size n.
 */
public class ValidParentheses{
  public static boolean isValid(String s){
    int n = s.length();
    // s.length() >= 1 is guaranteed
    Stack<Character> charStack = new Stack<>();
    charStack.push(s.charAt(0));
    for (int i = 1; i < n; i++){
      char c = s.charAt(i);
      // pop when a pair is found
      // empty means pair was just found, so push next character
      if (!charStack.isEmpty() && isPair(charStack.peek(), c)){
        charStack.pop();
      }
      else{
        charStack.push(c);
      }
    }
    return charStack.isEmpty();
  }

  // checks if two parentheses are a valid pair; a is opening and b is closing
  private static boolean isPair(char a, char b){
    if (a == '(' && b == ')')
      return true;
    if (a == '[' && b == ']')
      return true;
    if (a == '{' && b == '}')
      return true;
    return false;
  }
}
