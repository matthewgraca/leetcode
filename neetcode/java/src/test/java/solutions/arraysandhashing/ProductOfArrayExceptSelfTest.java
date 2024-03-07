package solutions.arraysandhashing;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import static solutions.arraysandhashing.ProductOfArrayExceptSelf.productExceptSelf;

import java.util.Arrays;

public class ProductOfArrayExceptSelfTest{
  @Test
  public void example1(){
    // initialize
    int[] input = {1,2,3,4};
    int[] expected = {24,12,8,6};
    int[] actual = productExceptSelf(input);

    // test
    String msg = "Expected " + Arrays.toString(expected) + 
      ", returned " + Arrays.toString(actual);
    assertTrue(msg, Arrays.equals(expected, actual));
  }

  @Test
  public void example2(){
    // initialize
    int[] input = {-1,1,0,-3,3};
    int[] expected = {0,0,9,0,0};
    int[] actual = productExceptSelf(input);

    // test
    String msg = "Expected " + Arrays.toString(expected) + 
      ", returned " + Arrays.toString(actual);
    assertTrue(msg, Arrays.equals(expected, actual));
  }
}
