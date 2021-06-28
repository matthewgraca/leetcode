package mgraca.medium;

import java.util.Queue;
import java.util.LinkedList;
import java.util.HashMap;

/*
 * Description: Given a string s, find the length of the longest substring without repeating 
 *  characters.
 *
 * Constraints:
 *  0 <= s.length <= 5 * 10^4
 *  s consists of English letters, digits, symbols and spaces.
 */
public class LongestSubstringWithoutRepeatingCharacters{
  public static int lengthOfLongestSubstringQueue(String s){
    Queue<Character> queue = new LinkedList<>();
    int longestLength = 0;
    for (int i = 0; i < s.length(); i++){
      // if a letter repeats, dequeue until the duplicate is gone
      while (queue.contains(s.charAt(i))){
        queue.remove();
      }
      queue.add(s.charAt(i));
      longestLength = Math.max(longestLength, queue.size());
    }
    return longestLength;
  }

  public static int lengthOfLongestSubstringSlidingWindow(String s){
    /*
    HashMap<Character, Integer> map = new HashMap<>();
    int leftWindow = 0;
    int rightWindow = 0;
    int longestLength = 0;
    while (rightWindow < s.length()){
      
      while (map.containsKey(s.charAt(rightWindow))){
        leftWindow++;
      }
      map.put(s.charAt(rightWindow), rightWindow);
      rightWindow++;
      longestLength = Math.max(longestLength, rightWindow - leftWindow);
    }
    return longestLength;
    */
    return 0;
  }
}
