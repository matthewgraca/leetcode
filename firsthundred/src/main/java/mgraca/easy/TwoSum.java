package mgraca.easy;

import java.util.HashMap;

/*
 * Description: Given an array of integers nums and an integer target, return indices of the two 
 *    numbers such that they add up to target.
 *  
 *  You may assume that each input would have exactly one solution, and you may not use the same 
 *    element twice.
 *
 *  You can return the answer in any order.
 *
 * Constraints:
 *  2 <= nums.length <= 10^4
 *  -10^9 <= nums[i] <= 10^9
 *  -10^9 <= target <= 10^9
 *  Only one valid answer exists.
 *
 *  Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
 *
 * Complexity (For fast):
 *  Time:   O(n)
 *  Space:  O(n)
 */
public class TwoSum{
  public static int[] naiveTwoSum(int[] nums, int target){
    int[] solution = null; // solution guaranteed, so no risk of returning null
    for (int i = 0; i < nums.length; i++){
      for (int j = i + 1; j < nums.length; j++){
        if (nums[i] + nums[j] == target){
          solution = new int[]{i, j};
        }
      }
    }
    return solution;
  }

  public static int[] fastTwoSum(int[] nums, int target){
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++){
      if (map.containsKey(target - nums[i])){
        return new int[]{map.get(target - nums[i]), i};
      }
      else{
        map.put(nums[i], i);
      }
    }
    return null;
  }
}
