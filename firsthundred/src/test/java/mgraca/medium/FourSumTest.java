package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

public class FourSumTest{
  @Test
  public void example1(){
    int[] input = new int[]{1,0,-1,0,-2,2};
    int target = 0;
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(Arrays.asList(-2,-1,1,2));
    expectedOutput.add(Arrays.asList(-2,0,0,2));
    expectedOutput.add(Arrays.asList(-1,0,0,1));
    List<List<Integer>> actualOutput = FourSum.fourSum(input, target);
    Collections.sort(actualOutput, new ListComparator<Integer>());
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example2(){
    int[] input = new int[]{2,2,2,2,2};
    int target = 8;
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(Arrays.asList(2,2,2,2));
    List<List<Integer>> actualOutput = FourSum.fourSum(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example3(){
    int[] input = new int[]{0,0,0,0};
    int target = 0;
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(Arrays.asList(0,0,0,0));
    List<List<Integer>> actualOutput = FourSum.fourSum(input, target);
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example4(){
    int[] input = new int[]{-2,-1,-1,1,1,2,2};
    int target = 0;
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(Arrays.asList(-2,-1,1,2));
    expectedOutput.add(Arrays.asList(-1,-1,1,1));
    List<List<Integer>> actualOutput = FourSum.fourSum(input, target);
    Collections.sort(actualOutput, new ListComparator<Integer>());
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example5(){
    int[] input = new int[]{-3,-1,0,2,4,5};
    int target = 1;
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(Arrays.asList(-3,-1,0,5));
    List<List<Integer>> actualOutput = FourSum.fourSum(input, target);
    Collections.sort(actualOutput, new ListComparator<Integer>());
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  @Test
  public void example6(){
    int[] input = new int[]{-1,0,1,2,-1,-4};
    int target = -1;
    List<List<Integer>> expectedOutput = new ArrayList<>();
    expectedOutput.add(Arrays.asList(-4,0,1,2));
    expectedOutput.add(Arrays.asList(-1,-1,0,1));
    List<List<Integer>> actualOutput = FourSum.fourSum(input, target);
    Collections.sort(actualOutput, new ListComparator<Integer>());
    String errorMsg = "Expected " + expectedOutput + ", returned " + actualOutput;
    assertTrue(errorMsg, actualOutput.equals(expectedOutput));
  }

  // allows us to sort list of lists
  private static class ListComparator<T extends Comparable<T>> implements Comparator<List<T>> {
    @Override
    public int compare(List<T> o1, List<T> o2) {
      for (int i = 0; i < Math.min(o1.size(), o2.size()); i++) {
        int c = o1.get(i).compareTo(o2.get(i));
        if (c != 0) {
          return c;
        }
      }
      return Integer.compare(o1.size(), o2.size());
    }
  }
}
