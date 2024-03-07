package solutions.twopointers;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

/*
 * https://leetcode.com/problems/3sum/
 *
 * Complexity
 *  Time: O(n^2)
 *    O(nlogn) to sort the array
 *    O(n^2) for the pointers to increment
 *  Space: O(n)
 *    O(n) is the number of distinct values that can be in a triple
 */
public class ThreeSum{
  public static List<List<Integer>> threeSum(int[] nums){
    List<List<Integer>> list = new ArrayList<>();
    Arrays.sort(nums);
    int n = nums.length;

    for (int i = 0; i < n-2; i++){
      int left = i+1;
      int right = n-1;
      while (left < right){
        int sum = nums[i] + nums[left] + nums[right];
        if (sum < 0)
          left++;
        else if (sum > 0)
          right--;
        else{
          list.add(Arrays.asList(nums[i], nums[left], nums[right]));
          left++;
          right--;
          // ensure next left and right pointers aren't repeating values
          while (left < right && nums[left-1] == nums[left])
            left++;
          while (left < right && nums[right+1] == nums[right])
            right--; 
        }
      }
      // ensure next nums[i] isn't a repeat
      while (i < n-3 && nums[i] == nums[i+1])
        i++;
    }

    return list;
  }

  public static List<List<Integer>> slowThreeSum(int[] nums){
    List<List<Integer>> list = new ArrayList<>();
    HashSet<List<Integer>> set = new HashSet<>();
    Arrays.sort(nums);
    int n = nums.length;
    for (int i = 0; i < n-2; i++){
      int left = i+1;
      int right = n-1;
      while (left < right){
        int sum = nums[i] + nums[left] + nums[right];
        if (sum < 0)
          left++;
        else if (sum > 0)
          right--;
        else{
          set.add(Arrays.asList(nums[i], nums[left], nums[right]));
          left++;
          right--;
        }
      }
    }
    list.addAll(set);
    return list;
  }
}
