package solutions.arraysandhashing;

import java.util.HashSet;
import java.util.ArrayList;
/*
 * https://leetcode.com/problems/longest-consecutive-sequence/
 *
 * Complexity
 *  Time: O(n)
 *    O(n) for adding n elements to the set
 *    O(n) for accessing nums to create the set
 *    O(n) for accessing nums to checking that element's neighbors
 *    O(n) for removing n elements from the set
 *  Space:  O(n)
 *    O(n) for the creation of a set of n elements
 */
public class LongestConsecutiveSequence{
  public static int longestConsecutive(int[] nums){
    // use set for O(1) access and prune duplicates
    HashSet<Integer> set = new HashSet<>();
    for (int i : nums){
      set.add(i);
    }

    // search the set
    int max = 0;
    for (int i = 0; !set.isEmpty(); i++){
      int count = 1;
      int current = nums[i];
      int left = current - 1;
      int right = current + 1;
      set.remove(current);

      // if current item has a neighbor, count them
      while (set.contains(right)){
        set.remove(right);
        count++;
        right++;
      }
      while (set.contains(left)){
        set.remove(left);
        count++;
        left--;
      }

      // take only the largest set of consecutive
      if (count > max)
        max = count;
    }
    return max;
  }
}
