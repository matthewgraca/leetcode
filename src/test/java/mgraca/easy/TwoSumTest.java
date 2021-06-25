package mgraca.easy;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class TwoSumTest{
  /*
   * These test the naive implementation
   */
  @Test
  public void naiveExample1(){
    int[] nums = new int[]{2, 7, 11, 15};
    int target = 9;
    int[] arr = TwoSum.naiveTwoSum(nums, target);
    assertTrue(arr[0] == 0 && arr[1] == 1);
  }

  @Test
  public void naiveExample2(){
    int[] nums = new int[]{3, 2, 4};
    int target = 6;
    int[] arr = TwoSum.naiveTwoSum(nums, target);
    assertTrue(arr[0] == 1 && arr[1] == 2);
  }

  @Test
  public void naiveExample3(){
    int[] nums = new int[]{3, 3};
    int target = 6;
    int[] arr = TwoSum.naiveTwoSum(nums, target);
    assertTrue(arr[0] == 0 && arr[1] == 1);
  }

  /*
   * These test the fast implementation
   */
  @Test
  public void fastExample1(){
    int[] nums = new int[]{2, 7, 11, 15};
    int target = 9;
    int[] arr = TwoSum.fastTwoSum(nums, target);
    assertTrue(arr[0] == 0 && arr[1] == 1);
  }

  @Test
  public void fastExample2(){
    int[] nums = new int[]{3, 2, 4};
    int target = 6;
    int[] arr = TwoSum.fastTwoSum(nums, target);
    assertTrue(arr[0] == 1 && arr[1] == 2);
  }

  @Test
  public void fastExample3(){
    int[] nums = new int[]{3, 3};
    int target = 6;
    int[] arr = TwoSum.fastTwoSum(nums, target);
    assertTrue(arr[0] == 0 && arr[1] == 1);
  }
}
