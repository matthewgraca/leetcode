package mgraca.easy;

import java.util.Collections;
import java.util.Arrays;
import java.util.List;
import java.lang.StringBuilder;

/*
 * Description: Write a function to find the longest common prefix string amongst an array of
 *  strings.
 *  If there is no common prefix, return an empty string "".
 *
 * Constraints:
 *  1 <= strs.length <= 200
 *  0 <= strs[i].length <= 200
 *  strs[i] consists of only lower-case English letters.
 * 
 * Complexity:
 *  Let n be the size of the array and m be the size of the smallest string.
 *  Time:   O(n+m)
 *    -n for copying array into a list, and scanning the list for the min and max
 *    -m for comparing strings and building the solution
 *  Space:  O(m)
 */
public class LongestCommonPrefix{
  public static String longestCommonPrefix(String[] strs){
    StringBuilder solution;
    if (strs.length == 1){
      solution = new StringBuilder(strs[0]);
    }
    else{
      solution = new StringBuilder();
      // find the largest and smallest strings
      List<String> list = Arrays.asList(strs);
      String smallest = Collections.min(list);
      String largest = Collections.max(list);

      // compare their prefixes
      int i = 0;
      boolean contScan = true;
      while (i < smallest.length() && contScan){
        if (smallest.charAt(i) == largest.charAt(i)){
          solution.append(smallest.charAt(i));
          i++;
        }
        else{
          contScan = false;
        }
      }
    }
    return solution.toString();
  }
}
