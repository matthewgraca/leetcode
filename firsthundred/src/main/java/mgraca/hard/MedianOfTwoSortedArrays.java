package mgraca.hard;

/*
 * Description: Given two sorted arrays nums1 and nums2 of size m and n respectively, 
 *  return the median of the two sorted arrays.
 *
 *  The overall run time complexity should be O(log (m+n)).
 *
 * Constraints:
 *  nums1.length == m
 *  nums2.length == n
 *  0 <= m <= 1000
 *  0 <= n <= 1000
 *  1 <= m + n <= 2000
 *  -10^6 <= nums1[i], nums2[i] <= 10^6
 *
 * Complexity:
 *  Time:   O(n+m)
 *  Space:  O(1)
 */
public class MedianOfTwoSortedArrays{
  public static double findMedianSortedArrays(int[] nums1, int[] nums2){
    double solution;
    int previous, current;

    // case 1: both arrays are empty
    if (nums1.length == 0 && nums2.length == 0){
      solution = 0;
    }
    // case 2: only nums1 is empty
    else if (nums1.length == 0 && nums2.length > 0){
      solution = medianOfANonEmptySortedArray(nums2);
    }
    // case 3: only nums2 is empty
    else if (nums1.length > 0 && nums2.length == 0){
      solution = medianOfANonEmptySortedArray(nums1);
    }
    // case 4: neither array is empty
    else{
      int i, j, k;
      i = j = k = 0;
      int totalLength = nums1.length + nums2.length;
      // set prev and curr to the global minimum value
      if (nums1[0] < nums2[0]){
        previous = current = nums1[0];
      }
      else{
        previous = current = nums2[0];
      }

      // increment until the median of the total array is reached
      while (k <= totalLength / 2){
        previous = current;
        // scan the other array if this one is finished
        if (i == nums1.length){
          current = nums2[j++];
        }
        else if (j == nums2.length){
          current = nums1[i++];
        }
        // otherwise, keep scanning for next minimum value
        else{
          if (nums1[i] < nums2[j]){
            current = nums1[i++];
          }
          else{
            current = nums2[j++];
          }
        }
        k++;
      }
      
      // handle even vs odd cardinality dataset
      if (totalLength % 2 == 0){
        solution = (previous + current) / 2.0;
      }
      else{
        solution = current;
      }
    }
    return solution;
  }

  /**
   * Finds the median of a single, non-empty, sorted array of ints
   * @param arr the array of ints
   * @return the median of the array of ints
   */
  private static double medianOfANonEmptySortedArray(int[] arr){
    // handle even vs odd cardinality
    if (arr.length % 2 == 0){
      return (arr[arr.length / 2] + arr[arr.length / 2 - 1]) / 2.0;
    }
    else{
      return arr[arr.length / 2];
    }
  }
}
