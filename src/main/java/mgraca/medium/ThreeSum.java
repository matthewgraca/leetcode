package mgraca.medium;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

/*
 * Description: Given an integer array nums, return all the triplets 
 *  [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and 
 *  nums[i] + nums[j] + nums[k] == 0.
 *  
 *  Notice that the solution set must not contain duplicate triplets.
 *
 * Constraints:
 *  0 <= nums.length <= 3000
 *  -10^5 <= nums[i] <= 10^5
 * 
 * Complexity:
 *  See below.
 */
public class ThreeSum{
  /*
   * Time:  O(n^3)
   * Space: O(n)
   */
  public static List<List<Integer>> naiveThreeSum(int[] nums){
    List<List<Integer>> solution = new ArrayList<>();
    Arrays.sort(nums);
    for (int i = 0; i < nums.length; i++){
      for (int j = i + 1; j < nums.length; j++){
        for (int k = j + 1; k < nums.length; k++){
          if (nums[i] + nums[j] + nums[k] == 0){
            List<Integer> solutionPiece = new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k]));
            if (!solution.contains(solutionPiece)){
              solution.add(solutionPiece);
            }
          }
        }
      }
    }
    return solution;
  }

  /*
   * Time:  
   * Space:
   */
  public static List<List<Integer>> fastThreeSum(int[] nums){
    List<List<Integer>> solution = new ArrayList<>();
    Arrays.sort(nums);
    return null;
  }
}
