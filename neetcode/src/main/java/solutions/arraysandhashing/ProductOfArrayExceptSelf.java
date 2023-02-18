package solutions.arraysandhashing;

/*
 * https://leetcode.com/problems/product-of-array-except-self/
 *
 * Important lesson: I was struggling with this all day, what enabled 
 *  me to break through was to code the things I know are required for 
 *  the solution. Afterwards, I was able to figure out how to fill out 
 *  the rest of the code to connect "what I knew MUST be the right code" 
 *  with the endpoint solution.
 *
 * Complexity
 *  Time:   O(n) 
 *    O(n) for the forward pass
 *    O(n) for the backward pass
 *  Space:  O(n)
 *    O(n) for the auxillary solution array (though the problem says 
 *      having an auxillary solution array doesn't count; in that case 
 *      we can say O(1))
 */
public class ProductOfArrayExceptSelf{
  public static int[] productExceptSelf(int[] nums){
    int prefix = 1;
    int suffix = 1;
    int[] solution = new int[nums.length];
    int n = nums.length;

    // scan forward to generate solution with only prefix products
    for (int i = 0; i < n; i++){
      solution[i] = prefix;
      prefix = prefix * nums[i];
    }

    // scan backwards to generate solution with suffix products
    for (int i = n-1; i >= 0; i--){
      solution[i] = suffix * solution[i];
      suffix = suffix * nums[i];
    }

    return solution;
  }
}
