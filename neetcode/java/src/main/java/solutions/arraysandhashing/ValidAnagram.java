package solutions.arraysandhashing;

import java.util.HashMap;
/*
 * https://leetcode.com/problems/valid-anagram/
 *
 * Complexity
 *  Time:   O(n) - n to increment through s, n to increment through t, 
 *    n to compare both tables.
 *  Space:  O(n) - n to store s, n to store t. 
 */
public class ValidAnagram{
  public static boolean isAnagram(String s, String t){
    // cannot be an anagram if t and s differ in length
    if (s.length() != t.length())
      return false;

    // put all of s into a hash table
    HashMap<Character, Integer> tableOfS = new HashMap<>();
    HashMap<Character, Integer> tableOfT = new HashMap<>();
    for (int i = 0; i < s.length(); i++){
      char currentSChar = s.charAt(i);
      char currentTChar = t.charAt(i);
      // keep count of the number of occurences of each character in s
      if (!tableOfS.containsKey(currentSChar))
        tableOfS.put(currentSChar, 1);
      else{
        int count = tableOfS.get(currentSChar);
        tableOfS.put(currentSChar, count+1); 
      }

      // same with t
      if (!tableOfT.containsKey(currentTChar))
        tableOfT.put(currentTChar, 1);
      else{
        int count = tableOfT.get(currentTChar);
        tableOfT.put(currentTChar, count+1); 
      }
    }

    // compare t to s
    return tableOfT.equals(tableOfS);
  }
}
