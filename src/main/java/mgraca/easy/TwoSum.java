package mgraca.easy;

import java.util.Random;

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
 * 2 <= nums.length <= 10^4
 * -10^9 <= nums[i] <= 10^9
 *  -10^9 <= target <= 10^9
 *  Only one valid answer exists.
 *
 *  Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
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
    int term1 = target;
    int term2 = 0;
    int i, j;
    i = j = 0;
    boolean foundBoth, foundOne, skip;
    foundBoth = foundOne = skip = false;
    
    // search for the two indeces that sum to target
    while (!foundBoth){
      // search for term1
      i = search(nums, term1, false);
      if (i == -1){
        foundOne = false;
      }
      else{
        foundOne = true;
      }
      // if term1 was found, search for term2
      if (foundOne){
        if (term1 == term2){
          skip = true;
        }
        j = search(nums, term2, skip);
        if (j == -1){
          foundBoth = false;
        }
        else{
          foundBoth = true;
        }
      }
      // otherwise, check the next combination of terms
      else{
        term1--;
        term2++;
      }
    }
    // keep index ordering from least -> greatest
    if (i < j){
      return new int[]{i, j};
    }
    else{
      return new int[]{j, i};
    }
  }

  /**
   * Searches for the element that contains the target integer
   * @param arr           the array being searched
   * @param target        the value being searched for
   * @param skipDuplicate tells method whether or not to skip the target once
   * @return if found, return the index of the target; else return -1
   */
  private static int search(int[] arr, int target, boolean skipDuplicate){
    boolean found = false;
    int i = 0;
    while (i < arr.length && !found){
      if (arr[i] == target){
        if (skipDuplicate){
          skipDuplicate = false;
          i++;
        }
        else{
          found = true;
        }
      }
      else{
        i++;
      }
    }
    if (found){
      return i;
    }
    else{
      return -1;
    }
  }
}
