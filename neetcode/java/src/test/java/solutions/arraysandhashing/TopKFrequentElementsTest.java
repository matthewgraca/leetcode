package solutions.arraysandhashing;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import static solutions.arraysandhashing.TopKFrequentElements.topKFrequent;

import java.util.Arrays;

public class TopKFrequentElementsTest{
  @Test
  public void example1(){
    // initialize
    int[] input1 = {1,1,1,2,2,3};
    int input2 = 2;
    int[] expected = {1,2};
    int[] actual = topKFrequent(input1, input2);
    Arrays.sort(actual);  // answer in any order
    Arrays.sort(expected);

    // test
    String msg =  "Expected " + Arrays.toString(expected) + 
                  ", returned " + Arrays.toString(actual); 
    assertTrue(msg, Arrays.equals(expected, actual));
  }

  @Test
  public void example2(){
    // initialize
    int[] input1 = {1};
    int input2 = 1;
    int[] expected = {1};
    int[] actual = topKFrequent(input1, input2);
    Arrays.sort(actual);  // answer in any order
    Arrays.sort(expected);

    // test
    String msg =  "Expected " + Arrays.toString(expected) + 
                  ", returned " + Arrays.toString(actual); 
    assertTrue(msg, Arrays.equals(expected, actual));
  }

  @Test
  public void example3(){
    // initialize
    int[] input1 = {1,1,1,2,2,2};
    int input2 = 2;
    int[] expected = {1,2};
    int[] actual = topKFrequent(input1, input2);
    Arrays.sort(actual);  // answer in any order
    Arrays.sort(expected);

    // test
    String msg =  "Expected " + Arrays.toString(expected) + 
                  ", returned " + Arrays.toString(actual); 
    assertTrue(msg, Arrays.equals(expected, actual));
  }
}
