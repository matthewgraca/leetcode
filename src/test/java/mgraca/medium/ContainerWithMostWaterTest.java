package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ContainerWithMostWaterTest{
  @Test
  public void example1(){
    int[] input = new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7};
    int expectedOutput = 49;
    int actualOutput = ContainerWithMostWater.maxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example2(){
    int[] input = new int[]{1, 1};
    int expectedOutput = 1;
    int actualOutput = ContainerWithMostWater.maxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example3(){
    int[] input = new int[]{4, 3, 2, 1, 4};
    int expectedOutput = 16;
    int actualOutput = ContainerWithMostWater.maxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example4(){
    int[] input = new int[]{1, 2, 1};
    int expectedOutput = 2;
    int actualOutput = ContainerWithMostWater.maxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }
}
