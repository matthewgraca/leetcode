package mgraca.medium;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

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
   * Time:  O(n^2)
   *  (adapted from wikipedia's pseudocode on 3sum)
   *  +nlogn for sorting
   *  +n^2 through iterating nums with 2 loops
   *  +n by copying the set onto an arraylist
   * Space: O(n^3)
   *  +n choose 3 -> worst case, every combination of triples is valid and stored
   */
  public static List<List<Integer>> wikiThreeSum(int[] nums){
    Set<List<Integer>> solution = new HashSet<>();
    Arrays.sort(nums);  
    for (int i = 0; i < nums.length - 2; i++){
      int a = nums[i];
      int start = i + 1;
      int end = nums.length - 1;
      while (start < end){
        int b = nums[start];
        int c = nums[end];
        if (a + b + c == 0){
          solution.add(new ArrayList<>(Arrays.asList(a, b, c)));
          start++;
          end--;
        }
        else if (a + b + c > 0){
          end--;
        }
        else{ // (a + b + c < 0)
          start++;
        }
      }
    }
    return new ArrayList<>(solution);
  }

  /*
   * Time:  O(n^2logn) 
   *  +nlogn for sorting
   *  +n^2logn for comparing each pair against a sorted value in the array using binary search 
   *  +adding a solution piece is O(1) since the underlying data structure is a map 
   *    (O(1) to check, O(1) to add)
   * Space: O(n^3)
   *  +worst case, every combination of triples is valid and stored
   */
  public static List<List<Integer>> sortThreeSum(int[] nums){
    Set<List<Integer>> solution = new HashSet<>();
    Arrays.sort(nums);
    for (int i = 0; i < nums.length; i++){
      for (int j = i + 1; j < nums.length; j++){
        int k = Arrays.binarySearch(nums, j+1, nums.length, -(nums[i]+nums[j]));
        if (k >= 0){
          solution.add(new ArrayList<>(Arrays.asList(nums[i], nums[j], nums[k])));
        }
      }
    }
    return new ArrayList<>(solution);
  }
}
