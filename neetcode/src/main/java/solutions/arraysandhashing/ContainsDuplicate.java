package solutions.arraysandhashing;

import java.util.HashSet;
/*
 * https://leetcode.com/problems/contains-duplicate/
 *
 * Complexity:
 *  Time:   O(n) - worst case, there are no duplicates and we must increment
 *    through the entire array.
 *  Space:  O(n) - worst case, there are no duplicates and we add to the set
 *    n times.
 */
public class ContainsDuplicate{
  public static boolean containsDuplicate(int[] nums){
    HashSet<Integer> hs = new HashSet<>();
    for (int i = 0; i < nums.length; i++){
      // if element was unable to add to set, a duplicate exists
      if (hs.add(nums[i]) == false)
        return true;
    }
    return false;
  }
}
