package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class ThreeSumTest{
  @Test
  public void wikiExample1(){
    int[] input = new int[]{-1, 0, 1, 2, -1, -4};
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(new ArrayList<>(Arrays.asList(-1, -1, 2)));
    expectedOutput.add(new ArrayList<>(Arrays.asList(-1, 0, 1)));

    List<List<Integer>> actualOutput = ThreeSum.wikiThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void wikiExample2(){
    int[] input = new int[0];
    List<List<Integer>> expectedOutput = new ArrayList<>();
    List<List<Integer>> actualOutput = ThreeSum.wikiThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void wikiExample3(){
    int[] input = new int[]{0};
    List<List<Integer>> expectedOutput = new ArrayList<>();
    List<List<Integer>> actualOutput = ThreeSum.wikiThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void sortExample1(){
    int[] input = new int[]{-1, 0, 1, 2, -1, -4};
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(new ArrayList<>(Arrays.asList(-1, -1, 2)));
    expectedOutput.add(new ArrayList<>(Arrays.asList(-1, 0, 1)));

    List<List<Integer>> actualOutput = ThreeSum.sortThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void sortExample2(){
    int[] input = new int[0];
    List<List<Integer>> expectedOutput = new ArrayList<>();
    List<List<Integer>> actualOutput = ThreeSum.sortThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void sortExample3(){
    int[] input = new int[]{0};
    List<List<Integer>> expectedOutput = new ArrayList<>();
    List<List<Integer>> actualOutput = ThreeSum.sortThreeSum(input);
    String errorMsg = "Expected " + expectedOutput.toString() + 
                      ", returned " + actualOutput.toString();
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }
}
