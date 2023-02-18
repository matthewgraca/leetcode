package mgraca.medium;

/*
 * Description: Given n non-negative integers a1, a2, ..., an , where each represents a point at 
 *  coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at 
 *  (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that
 *  the container contains the most water.
 *
 *  Notice that you may not slant the container.
 *
 * Constraints:
 *  n == height.length
 *  2 <= n <= 10^5
 *  0 <= height[i] <= 10^4
 *
 * Complexity:
 *  Time:
 *  Space:
 */
public class ContainerWithMostWater{
  /*
   * Time:  O(n^2)
   * Space: O(1)
   */
  public static int naiveMaxArea(int[] height){
    int largestArea = 0;
    int lowerHeight = 0;
    for (int i = 0; i < height.length; i++){
      for (int j = i + 1; j < height.length; j++){
        lowerHeight = Math.min(height[i], height[j]);
        largestArea = Math.max(lowerHeight * (j - i), largestArea);
      }
    }
    return largestArea;
  }

  /*
   * Time:  O(n) 
   * Space: O(1)
   */
  public static int fastMaxArea(int[] height){
    int left = 0;
    int right = height.length - 1;
    int area = Math.min(height[left], height[right]) * (right - left);
    while (left < right){
      if (height[left] < height[right]){
        left++;
      }
      else{
        right--;
      }
      area = Math.max(area, Math.min(height[left], height[right]) * (right - left));
    }
    return area;
  }
}
