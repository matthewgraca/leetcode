package mgraca.hard;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class MedianOfTwoSortedArraysTest{
  @Test
  public void example1(){
    int[] nums1 = new int[]{1, 3};
    int[] nums2 = new int[]{2};
    assertTrue(MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2) == 2);
  }

  @Test
  public void example2(){
    int[] nums1 = new int[]{1, 2};
    int[] nums2 = new int[]{3, 4};
    assertTrue(MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2) == 2.5);
  }

  @Test
  public void example3(){
    int[] nums1 = new int[2];
    int[] nums2 = new int[2];
    assertTrue(MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2) == 0);
  }

  @Test
  public void example4(){
    int[] nums1 = new int[0];
    int[] nums2 = new int[]{1};
    assertTrue(MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2) == 1);
  }

  @Test
  public void example5(){
    int[] nums1 = new int[]{2};
    int[] nums2 = new int[0];
    assertTrue(MedianOfTwoSortedArrays.findMedianSortedArrays(nums1, nums2) == 2);
  }
}
