package mgraca.medium;

import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

/*
 * Description: Given an array nums of n integers, return an array of all the unique quadruplets 
 *  [nums[a], nums[b], nums[c], nums[d]] such that:
 *  0 <= a, b, c, d < n
 *  a, b, c, and d are distinct.
 *  nums[a] + nums[b] + nums[c] + nums[d] == target
 *
 *  You may return the answer in any order.
 *
 * Constraints:
 *  1 <= nums.length <= 200
 *  -10^9 <= nums[i] <= 10^9
 *  -10^9 <= target <= 10^9
 *
 * Complexity:
 *  Time:   O(n^3)
 *    + 3 nested loops that iterate through the whole array
 *    + while adding to the set is O(1), it takes O(n) to copy the set into a List
 *  Space:  O(n^4)
 *    - every single quadruple is valid and stored
 */
public class FourSum{
  public static List<List<Integer>> fourSum(int[] nums, int target){
    Set<List<Integer>> solution = new HashSet<>();
    if (nums.length < 4){
      // return empty list
    }
    else{
      Arrays.sort(nums);
      for (int i = 0; i < nums.length - 3; i++){
        int a = nums[i];
        for (int j = i + 1; j < nums.length - 2; j++){
          int b = nums[j];
          int start = j + 1;
          int end = nums.length - 1;
          while (start < end){
            int c = nums[start];
            int d = nums[end];
            if (a + b + c + d == target){
              solution.add(Arrays.asList(a, b, c, d));
              start++;
              end--;
            }
            else if (a + b + c + d > target){
              end--;
            }
            else{// a + b + c + d < target
              start++;
            }
          }
        }
      }
    }
    return new ArrayList<>(solution);
  }
}
