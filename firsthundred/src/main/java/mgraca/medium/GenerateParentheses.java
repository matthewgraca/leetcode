package mgraca.medium;

import mgraca.ListNode;
import java.util.List;
import java.util.ArrayList;

/*
 * Description: Given n pairs of parentheses, write a function to generate all 
 *  combinations of well-formed parentheses.
 *
 * Constraints:
 *  1 <= n <= 8
 * 
 * Complexity:
 *  Discussion: both are O(4^(n)/sqrt(n)); my best guess was that this 
 *    is a binary tree; 2^(n*2), where n*2 is the height of the tree; 
 *    which would be O(4^n). Since backtracking works by pruning a ton of 
 *    invalid solutions, the sqrt(n) makes sense.
 */
public class GenerateParentheses{
  public static List<String> generateParenthesis(int n){
    List<String> solution = new ArrayList<>();
    backtrack(solution, new String(), 0, 0, n);
    return solution;
  }

  /**
   * Backtracking solution to generating parenthesis
   * @param solution  the list containing all valid combinations
   * @param s         the string of parentheses being built and checked
   * @param open      the number of open parentheses in the current string
   * @param close     the number of closed parentheses in the current string
   * @param n         the max size of a valid string (depth to stop, x2)
   */
  private static void backtrack(List<String> solution, String s, 
                                int open, int close, int n){
    if (s.length() == n*2){
      solution.add(s);
      return;
    }

    if (open < n){
      s = s + "(";
      backtrack(solution, s, open+1, close, n);
      s = s.substring(0, s.length()-1);
    }
    if (close < open){  // matches closing with opening
      s = s + ")";
      backtrack(solution, s, open, close+1, n);
      s = s.substring(0, s.length()-1);
    }
    // no solution can be built from here; return and look at other strings 
    return;
  }
}
