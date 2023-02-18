package solutions.arraysandhashing;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

import static solutions.arraysandhashing.TwoSum.twoSum;
import java.util.Arrays;

public class TwoSumTest{
  @Test
  public void example1(){
    // init inputs
    int[] input1 = {2,7,11,15};
    int input2 = 9;

    // format outputs; ignore order
    int[] actual = twoSum(input1, input2);
    Arrays.sort(actual);
    int[] expected = {0,1};
    Arrays.sort(expected);

    // test
    String msg =  "Expected " + Arrays.toString(expected) + ", returned " 
                  + Arrays.toString(actual);
    assertTrue(msg, Arrays.equals(actual, expected));
  }

  @Test
  public void example2(){
    // init inputs
    int[] input1 = {3,2,4};
    int input2 = 6;

    // format outputs; ignore order
    int[] actual = twoSum(input1, input2);
    Arrays.sort(actual);
    int[] expected = {1,2};
    Arrays.sort(expected);

    // test
    String msg =  "Expected " + Arrays.toString(expected) + ", returned " 
                  + Arrays.toString(actual);
    assertTrue(msg, Arrays.equals(actual, expected));
  }

  @Test
  public void example3(){
    // init inputs
    int[] input1 = {3,3};
    int input2 = 6;

    // format outputs; ignore order
    int[] actual = twoSum(input1, input2);
    Arrays.sort(actual);
    int[] expected = {0,1};
    Arrays.sort(expected);

    // test
    String msg =  "Expected " + Arrays.toString(expected) + ", returned " 
                  + Arrays.toString(actual);
    assertTrue(msg, Arrays.equals(actual, expected));
  }
}
