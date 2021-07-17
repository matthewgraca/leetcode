package mgraca.easy;

import java.util.HashMap;

/*
 * Description: Given a roman numeral, convert it to an integer
 *
 * Constraints:
 *  1 <= s.length <= 15
 *  s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
 *  It is guaranteed that s is a valid roman numeral in the range [1, 3999].
 *
 * Complexity:
 *  Time:
 *  Space:
 */
public class RomanToInteger{
  public static int romanToInt(String s){
    HashMap<Character, Integer> map = initializeRomanToIntegerMap();
    int prevLetter = map.get(s.charAt(0));
    int currentLetter;
    int solution = prevLetter;
    for (int i = 1; i < s.length(); i++){
      currentLetter = map.get(s.charAt(i));
      if (prevLetter < currentLetter){
        solution -= prevLetter * 2;
        solution += currentLetter;
      }
      else{
        solution += currentLetter;
      }
      prevLetter = currentLetter;
    }
    return solution;
  }

  /**
   * Initializes a hash map that maps Roman letters to integers
   * @return  the map that contains the mapping of roman letters to integers
   */
  private static HashMap<Character, Integer> initializeRomanToIntegerMap(){
    HashMap<Character, Integer> map = new HashMap<>();
    map.put('I', 1);
    map.put('V', 5);
    map.put('X', 10);
    map.put('L', 50);
    map.put('C', 100);
    map.put('D', 500);
    map.put('M', 1000);
    return map;
  }
}
