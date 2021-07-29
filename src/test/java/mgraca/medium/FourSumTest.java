package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class FourSumTest{
  @Test
  public void example1(){
    int[] input = new int[]{1,0,-1,0,-2,2};
    int target = 0;
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(new ArrayList<>(Arrays.asList(-2,-1,1,2)));
    expectedOutput.add(new ArrayList<>(Arrays.asList(-2,0,0,2)));
    expectedOutput.add(new ArrayList<>(Arrays.asList(-1,0,0,1)));
    List<List<Integer>> actualOutput = FourSum.fourSum(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example2(){
    int[] input = new int[]{2,2,2,2,2};
    int target = 8;
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(new ArrayList<>(Arrays.asList(2,2,2,2)));
    List<List<Integer>> actualOutput = FourSum.fourSum(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }
}
