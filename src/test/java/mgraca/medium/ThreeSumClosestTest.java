package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ThreeSumClosestTest{
  @Test
  public void naiveExample1(){
    int[] input = new int[]{-1, 2, 1, -4};
    int target = 1;
    int expectedOutput = 2;
    int actualOutput = ThreeSumClosest.naiveThreeSumClosest(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput == expectedOutput);
  }

  @Test
  public void naiveExample2(){
    int[] input = new int[]{-1, 0, 1, 2, -1, -4};
    int target = 0;
    int expectedOutput = 0;
    int actualOutput = ThreeSumClosest.naiveThreeSumClosest(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput == expectedOutput);
  }

  @Test
  public void sortExample1(){
    int[] input = new int[]{-1, 2, 1, -4};
    int target = 1;
    int expectedOutput = 2;
    int actualOutput = ThreeSumClosest.sortThreeSumClosest(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput == expectedOutput);
  }

  @Test
  public void sortExample2(){
    int[] input = new int[]{-1, 0, 1, 2, -1, -4};
    int target = 0;
    int expectedOutput = 0;
    int actualOutput = ThreeSumClosest.sortThreeSumClosest(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput == expectedOutput);
  }

  @Test
  public void sortExample3(){
    int[] input = new int[]{1, 1, 1, 0};
    int target = -100;
    int expectedOutput = 2;
    int actualOutput = ThreeSumClosest.sortThreeSumClosest(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput == expectedOutput);
  }

  @Test
  public void sortExample4(){
    int[] input = new int[]{1, 2, 4, 8, 16, 32, 64, 128};
    int target = 82;
    int expectedOutput = 82;
    int actualOutput = ThreeSumClosest.sortThreeSumClosest(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput == expectedOutput);
  }

}
