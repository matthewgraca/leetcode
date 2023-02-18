package mgraca.medium;

import java.util.Arrays;

/*
 * Description: Given an array nums of n integers and an integer target, find three integers in 
 *  nums such that the sum is closest to target. Return the sum of the three integers. 
 *  You may assume that each input would have exactly one solution.
 *  
 * Constraints:
 *  3 <= nums.length <= 10^3
 *  -10^3 <= nums[i] <= 10^3
 *  -10^4 <= target <= 10^4
 * 
 * Complexity:
 *  See below.
 */
public class ThreeSumClosest{
  /*
   * Let n be the size of the array of integers.
   * Time:  O(n^3)
   * Space: O(1)
   */
  public static int naiveThreeSumClosest(int[] nums, int target){
    int minDistance = Math.abs(target - (nums[0] + nums[1] + nums[2]));
    int bestSum = nums[0] + nums[1] + nums[2]; 
    for (int i = 0; i < nums.length; i++){
      for (int j = i + 1; j < nums.length; j++){
        for (int k = j + 1; k < nums.length; k++){
          int currSum = nums[i] + nums[j] + nums[k];
          int currDistance = Math.min(minDistance, Math.abs(target - currSum));
          if (minDistance > currDistance){
            minDistance = currDistance;
            bestSum = currSum;
          }
        }
      }
    }
    return bestSum;
  }

  /*
   * Time:  O(n^2)
   * Space: O(1)
   */
  public static int sortThreeSumClosest(int[] nums, int target){
    Arrays.sort(nums);
    int minDistance = Math.abs(target - (nums[0] + nums[1] + nums[2]));
    int bestSum = nums[0] + nums[1] + nums[2]; 
    for (int i = 0; i < nums.length - 2; i++){
      int a = nums[i];
      int start = i + 1;
      int end = nums.length - 1;
      while (start < end){
        int b = nums[start];
        int c = nums[end];
        int currDistance = Math.abs(target - (a + b + c));
        int currSum = a + b + c;
        // exit if we reaced the target
        if (currSum == target){
          return target;
        }
        // reduce the sum if we move away from the target
        else if (currSum > target){
          end--;
        }
        // increase the sum if we're moving towards the target
        else{
          start++;
        }
        // if the distance improves, set that as the new closest
        if (currDistance < minDistance){
          minDistance = currDistance;
          bestSum = a + b + c;
        }
      }
    }
    return bestSum;
  }
}
