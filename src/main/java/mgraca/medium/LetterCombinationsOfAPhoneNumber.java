package mgraca.medium;

import java.util.List;
import java.util.Arrays;
import java.util.HashMap;
import java.util.ArrayList;

/*
 * Description: Given a string containing digits from 2-9 inclusive, return all possible letter 
 *  combinations that the number could represent. Return the answer in any order.
 *
 *  A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 
 *    does not map to any letters.
 *
 * Constraints:
 *  0 <= digits.length <= 4
 *  digits[i] is a digit in the range ['2', '9'].
 * 
 * Complexity:
 *  See below.
 */
public class LetterCombinationsOfAPhoneNumber{
  /*
   * Iterative solution for the problem.
   * Let n be the length of digits.
   * Time:  O(4^n)
   *  +There are 4^n possible solutions if '7' or '9' is chosen, 3^n for any other digit
   * Space: O(4^n)
   */
  public static List<String> itLetterCombinations(String digits){
    List<String> solution = new ArrayList<>();
    if (digits.length() == 0){
      return solution;
    }
    else{
      // initialize the solution
      HashMap<Character, String[]> map = initializePhoneMap();
      for (int i = 0; i < map.get(digits.charAt(0)).length; i++){
        solution.add(map.get(digits.charAt(0))[i]);
      }
      // check the next digit
      for (int i = 1; i < digits.length(); i++){
        List<String> sol = new ArrayList<>();
        // grab each solution
        for (int j = 0; j < solution.size(); j++){
          // append each solution with all 3-4 combinations from the digit
          String[] numsFromCurrentDigit = map.get(digits.charAt(i));
          for (int k = 0; k < numsFromCurrentDigit.length; k++){
            sol.add(solution.get(j) + numsFromCurrentDigit[k]);
          }
        }
        solution = sol;
      }
      return solution;
    }
  }

  /**
   * Initializes the hash table that maps 2-9 to the alphabet, in the form of a phone
   * @return the hash table that maps 2-9 to the alphabet
   */
  private static HashMap<Character, String[]> initializePhoneMap(){
    HashMap<Character, String[]> map = new HashMap<>();
    map.put('2', new String[]{"a","b","c"});
    map.put('3', new String[]{"d","e","f"});
    map.put('4', new String[]{"g","h","i"});
    map.put('5', new String[]{"j","k","l"});
    map.put('6', new String[]{"m","n","o"});
    map.put('7', new String[]{"p","q","r", "s"});
    map.put('8', new String[]{"t","u","v"});
    map.put('9', new String[]{"w","x","y","z"});
    return map;
  }
}
