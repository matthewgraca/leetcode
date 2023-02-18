package solutions.twopointers;

import static org.junit.Assert.assertTrue;
import org.junit.Test;
import static solutions.twopointers.ThreeSum.threeSum;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

public class ThreeSumTest{
  private boolean equals(List<List<Integer>> l1, List<List<Integer>> l2){
    // ensure both list contains the same triples
    l1.sort(new ListComparator<>());
    l2.sort(new ListComparator<>());
    return l1.equals(l2);
  }

  @Test
  public void example1(){
    int[] input = {-1,0,1,2,-1,-4};
    List<List<Integer>> expected = new ArrayList<>();
    expected.add(Arrays.asList(-1,-1,2));
    expected.add(Arrays.asList(-1,0,1));
    List<List<Integer>> actual = threeSum(input); 

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, equals(expected, actual));
  }

  @Test
  public void example2(){
    int[] input = {0,1,1};
    List<List<Integer>> expected = new ArrayList<>();
    List<List<Integer>> actual = threeSum(input); 

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, equals(expected, actual));
  }

  @Test
  public void example3(){
    int[] input = {0,0,0};
    List<List<Integer>> expected = new ArrayList<>();
    expected.add(Arrays.asList(0,0,0));
    List<List<Integer>> actual = threeSum(input); 

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, equals(expected, actual));
  }

  @Test
  public void example4(){
    int[] input = {-2,0,0,2,2};
    List<List<Integer>> expected = new ArrayList<>();
    expected.add(Arrays.asList(-2,0,2));
    List<List<Integer>> actual = threeSum(input); 

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, equals(expected, actual));
  }

  @Test
  public void example5(){
    int[] input = {-2,0,1,1,2};
    List<List<Integer>> expected = new ArrayList<>();
    expected.add(Arrays.asList(-2,0,2));
    expected.add(Arrays.asList(-2,1,1));
    List<List<Integer>> actual = threeSum(input); 

    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, equals(expected, actual));
  }
}

class ListComparator<T extends Comparable<T>> implements Comparator<List<T>>{
  @Override
  public int compare(List<T> o1, List<T> o2){
    for (int i = 0; i < Math.min(o1.size(), o2.size()); i++) {
      int c = o1.get(i).compareTo(o2.get(i));
      if (c != 0) {
        return c;
      }
    }
    return Integer.compare(o1.size(), o2.size());
  }
}
