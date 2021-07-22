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
   * Time:  O(n^9)
   *  +nlogn for sorting
   *  +n choose 3 -> compare all combinations of 3 from n items, each with 
   *    3 * (n^3 choose 2) -> worst case, all solution triples are valid and checked 
   *    worst case: add 1 check 1, add 1 check 2, add 1 check 3, ..., add 1 check n
   * Space: O(n^3)
   *  +n choose 3 -> worst case, every combination of triples is valid and stored
   */
  public static List<List<Integer>> naiveThreeSum(int[] nums){
    List<List<Integer>> solution = new ArrayList<>();
    Arrays.sort(nums);  // ensures the triples are sorted
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
   * Time:  O(n^8logn) 
   *  +nlogn for sorting
   *  +n^2logn for comparing each pair against a sorted value in the array using binary search 
   *  +3 * n^3 choose 2 = n^6, worst case every triple is valid and checked against
   * Space: O(n^3)
   *  +worst case, every combination of triples is valid and stored
   */
  public static List<List<Integer>> sortThreeSum(int[] nums){
    List<List<Integer>> solution = new ArrayList<>();
    Arrays.sort(nums);
    for (int i = 0; i < nums.length; i++){
      for (int j = i + 1; j < nums.length; j++){
        int k = Arrays.binarySearch(nums, j+1, nums.length, -(nums[i]+nums[j]));
        if (k >= 0){
          List<Integer> solutionPiece = new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k]));
          if (!solution.contains(solutionPiece)){
            solution.add(solutionPiece);
          }
        }
      }
    }
    return solution;
  }

  public static List<List<Integer>> hashThreeSum(int[] nums){
    return null;
  }
}
