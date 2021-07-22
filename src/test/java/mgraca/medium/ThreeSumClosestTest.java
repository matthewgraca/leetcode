package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ThreeSumClosestTest{
  @Test
  public void example1(){
    int[] input = new int[]{-1, 2, 1, -4};
    int target = 1;
    int expectedOutput = 2;
    int actualOutput = ThreeSumClosest.threeSumClosest(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput == expectedOutput);
  }
}
