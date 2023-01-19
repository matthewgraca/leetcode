package mgraca.medium;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import mgraca.ListNode;

public class SwapNodesInPairsTest{
  @Test
  public void example1(){
    // initialize input and output
    ListNode input = null;
    ListNode output = SwapNodesInPairs.swapPairs(input);

    // cast actual to arraylist for easy comparison
    ArrayList<Integer> expected = new ArrayList<>();
    ArrayList<Integer> actual = new ArrayList<>();
    for (ListNode temp = output; temp != null; temp = temp.next){
      actual.add(temp.val);
    }

    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected.equals(actual));
  }

  @Test
  public void example2(){
    // initialize input and output
    ListNode input = new ListNode(1, null);
    ListNode output = SwapNodesInPairs.swapPairs(input);

    // cast actual to arraylist for easy comparison
    ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(1));
    ArrayList<Integer> actual = new ArrayList<>();
    for (ListNode temp = output; temp != null; temp = temp.next){
      actual.add(temp.val);
    }

    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected.equals(actual));
  }

  @Test
  public void example3(){
    // initialize input and output
    ListNode input =  new ListNode(1, new ListNode
                                  (2, new ListNode
                                  (3, new ListNode
                                  (4, null))));
    ListNode output = SwapNodesInPairs.swapPairs(input);

    // cast actual to arraylist for easy comparison
    ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(2,1,4,3));
    ArrayList<Integer> actual = new ArrayList<>();
    for (ListNode temp = output; temp != null; temp = temp.next){
      actual.add(temp.val);
    }

    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected.equals(actual));
  }
}
