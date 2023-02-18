package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ContainerWithMostWaterTest{
  @Test
  public void example1Naive(){
    int[] input = new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7};
    int expectedOutput = 49;
    int actualOutput = ContainerWithMostWater.naiveMaxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example2Naive(){
    int[] input = new int[]{1, 1};
    int expectedOutput = 1;
    int actualOutput = ContainerWithMostWater.naiveMaxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example3Naive(){
    int[] input = new int[]{4, 3, 2, 1, 4};
    int expectedOutput = 16;
    int actualOutput = ContainerWithMostWater.naiveMaxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example4Naive(){
    int[] input = new int[]{1, 2, 1};
    int expectedOutput = 2;
    int actualOutput = ContainerWithMostWater.naiveMaxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example1Fast(){
    int[] input = new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7};
    int expectedOutput = 49;
    int actualOutput = ContainerWithMostWater.fastMaxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example2Fast(){
    int[] input = new int[]{1, 1};
    int expectedOutput = 1;
    int actualOutput = ContainerWithMostWater.fastMaxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example3Fast(){
    int[] input = new int[]{4, 3, 2, 1, 4};
    int expectedOutput = 16;
    int actualOutput = ContainerWithMostWater.fastMaxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example4Fast(){
    int[] input = new int[]{1, 2, 1};
    int expectedOutput = 2;
    int actualOutput = ContainerWithMostWater.fastMaxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }

  @Test
  public void example5Fast(){
    int[] input = new int[]{2, 3, 4, 5, 18, 17, 6};
    int expectedOutput = 17;
    int actualOutput = ContainerWithMostWater.fastMaxArea(input);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, expectedOutput == actualOutput); 
  }
}
