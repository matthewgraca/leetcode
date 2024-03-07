package solutions.twopointers;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import static solutions.twopointers.TwoSumII.twoSum;

import java.util.Arrays;

public class TwoSumIITest{
  @Test
  public void example1(){
    // init inputs and outputs
    int[] input1 = {2,7,11,15};
    int input2 = 9;
    int[] expected = {1,2};
    int[] actual = twoSum(input1, input2);

    // test
    String msg =  "Expected " + Arrays.toString(expected) + 
                  ", returned " + Arrays.toString(actual);
    assertTrue(msg, Arrays.equals(expected, actual));
  }

  @Test
  public void example2(){
    // init inputs and outputs
    int[] input1 = {2,3,4};
    int input2 = 6;
    int[] expected = {1,3};
    int[] actual = twoSum(input1, input2);

    // test
    String msg =  "Expected " + Arrays.toString(expected) + 
                  ", returned " + Arrays.toString(actual);
    assertTrue(msg, Arrays.equals(expected, actual));
  }

  @Test
  public void example3(){
    // init inputs and outputs
    int[] input1 = {-1,0};
    int input2 = -1;
    int[] expected = {1,2};
    int[] actual = twoSum(input1, input2);

    // test
    String msg =  "Expected " + Arrays.toString(expected) + 
                  ", returned " + Arrays.toString(actual);
    assertTrue(msg, Arrays.equals(expected, actual));
  }
}
