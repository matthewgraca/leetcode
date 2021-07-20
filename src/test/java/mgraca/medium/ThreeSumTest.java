package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class ThreeSumTest{
  @Test
  public void naiveExample1(){
    int[] input = new int[]{-1, 0, 1, 2, -1, -4};
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(new ArrayList<>(Arrays.asList(-1, -1, 2)));
    expectedOutput.add(new ArrayList<>(Arrays.asList(-1, 0, 1)));

    List<List<Integer>> actualOutput = ThreeSum.naiveThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void naiveExample2(){
    int[] input = new int[0];
    List<List<Integer>> expectedOutput = new ArrayList<>();
    List<List<Integer>> actualOutput = ThreeSum.naiveThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void naiveExample3(){
    int[] input = new int[]{0};
    List<List<Integer>> expectedOutput = new ArrayList<>();
    List<List<Integer>> actualOutput = ThreeSum.naiveThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void fastExample1(){
    int[] input = new int[]{-1, 0, 1, 2, -1, -4};
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(new ArrayList<>(Arrays.asList(-1, -1, 2)));
    expectedOutput.add(new ArrayList<>(Arrays.asList(-1, 0, 1)));

    List<List<Integer>> actualOutput = ThreeSum.fastThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void fastExample2(){
    int[] input = new int[0];
    List<List<Integer>> expectedOutput = new ArrayList<>();
    List<List<Integer>> actualOutput = ThreeSum.fastThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void fastExample3(){
    int[] input = new int[]{0};
    List<List<Integer>> expectedOutput = new ArrayList<>();
    List<List<Integer>> actualOutput = ThreeSum.fastThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

}
