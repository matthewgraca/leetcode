package solutions.arraysandhashing;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import static solutions.arraysandhashing.LongestConsecutiveSequence.*;

public class LongestConsecutiveSequenceTest{
  @Test
  public void example1(){
    // init
    int[] input = {100,4,200,1,3,2};
    int expected = 4;
    int actual = longestConsecutive(input);

    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }

  @Test
  public void example2(){
    // init
    int[] input = {0,3,7,2,5,8,4,6,0,1};
    int expected = 9;
    int actual = longestConsecutive(input);

    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected == actual);
  }
}
