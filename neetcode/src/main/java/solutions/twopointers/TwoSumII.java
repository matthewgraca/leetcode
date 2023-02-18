package solutions.twopointers;

import java.util.HashMap;

/*
 * https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
 *
 * Complexity
 *  Time: O(n)
 *    O(n) to increment through numbers
 *  Space: O(1)
 *    O(1) uses same amount of memory regardless of the size of numbers
 */
public class TwoSumII{
  public static int[] twoSum(int[] numbers, int target){
    int left = 0;
    int right = numbers.length - 1;
    while (left != right){ 
      int sum = numbers[left] + numbers[right];
      if (sum < target)
        left++;
      else if (sum > target)
        right--;
      else
        return new int[]{left+1, right+1};
    }
    return new int[]{};
  }
}
