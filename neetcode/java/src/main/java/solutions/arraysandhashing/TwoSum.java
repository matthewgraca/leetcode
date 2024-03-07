package solutions.arraysandhashing;

import java.util.HashMap;
/*
 * https://leetcode.com/problems/two-sum/
 *
 * Explanation: If the other operand is not found, we add the current operand 
 *  to the map. That way, when the other operand is reached, it can find the 
 *  operand that previously conducted the search. This prevents repeat 
 *  solutions from being considered as the same.
 *
 * Complexity
 *  Time:   O(n) - if no target is found the entire nums array is incremented 
 *  Space:  O(n) - if no target is found, a map of size n is filled
 */
public class TwoSum{
  public static int[] twoSum(int[] nums, int target){
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++){
      int diff = target - nums[i];
      if (map.containsKey(diff))
        return new int[]{map.get(diff), i};
      else
        map.put(nums[i], i);
    }
    return null;
  }
}
