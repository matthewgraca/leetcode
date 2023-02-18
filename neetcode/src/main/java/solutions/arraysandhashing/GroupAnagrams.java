package solutions.arraysandhashing;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
/*
 * https://leetcode.com/problems/group-anagrams/
 *
 * Complexity
 *  Time:
 *    Let n be the total size of all the strings
 *    Let s be the total number of strings
 *    O(n) for copying all strings to character arrays, letter by letter
 *    O(nlogn) for sorting all the strings
 *    O(s) for adding all the strings into a map
 *    O(s) for iterating through all the strings in the map
 *    Total: O(nlogn + s)
 *  Space:
 *    O(n + s) for the character array, map, and the solution
 */
public class GroupAnagrams{
  public static List<List<String>> groupAnagrams(String[] strs){
    ArrayList<String> sortedStrs = new ArrayList<>();
    HashMap<String, ArrayList<Integer>> map = new HashMap<>();
    for (int i = 0; i < strs.length; i++){
      // create sorted aux string array
      char[] strChar = strs[i].toCharArray();
      Arrays.sort(strChar);
      sortedStrs.add(new String(strChar));

      // group anagrams under same key, with their index in strs[] as the value 
      if (!map.containsKey(sortedStrs.get(i)))
        map.put(sortedStrs.get(i), new ArrayList<Integer>());
      map.get(sortedStrs.get(i)).add(i);
    }

    // build solution
    List<List<String>> solution = new ArrayList<>();
    for (HashMap.Entry<String, ArrayList<Integer>> hm : map.entrySet()){
      // iterate through each key, group the indeces associated with each key
      ArrayList<Integer> val = hm.getValue();
      ArrayList<String> group = new ArrayList<>();
      for (Integer i : val)
        group.add(strs[i]);
      solution.add(group);
    }

    return solution;
  }
}
