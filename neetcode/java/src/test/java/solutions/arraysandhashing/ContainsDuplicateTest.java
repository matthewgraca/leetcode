package solutions.arraysandhashing;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

public class ContainsDuplicateTest{
  @Test
  public void example1(){
    int[] input = {1,2,3,1};
    boolean expected = true;
    boolean actual = ContainsDuplicate.containsDuplicate(input);
    assertTrue(actual == expected);
  }

  @Test
  public void example2(){
    int[] input = {1,2,3,4};
    boolean expected = false;
    boolean actual = ContainsDuplicate.containsDuplicate(input);
    assertTrue(actual == expected);
  }

  @Test
  public void example3(){
    int[] input = {1,1,1,3,3,4,3,2,4,2};
    boolean expected = true;
    boolean actual = ContainsDuplicate.containsDuplicate(input);
    assertTrue(actual == expected);
  }
}
