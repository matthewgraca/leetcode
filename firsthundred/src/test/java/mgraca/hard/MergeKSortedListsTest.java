package mgraca.hard;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

import mgraca.ListNode;
import java.util.ArrayList;
import java.util.Arrays;

public class MergeKSortedListsTest{
  @Test
  public void example1(){
    // initialize input, expected output, and actual output 
    ListNode[] input = null;
    ArrayList<Integer> expected = new ArrayList<>();
    ListNode output = MergeKSortedLists.mergeKLists(input);

    // cast output from ListNode to ArrayList for easy comparison
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
    // initialize input, expected output, and actual output 
    ListNode[] input = new ListNode[1];
    ArrayList<Integer> expected = new ArrayList<>();
    ListNode output = MergeKSortedLists.mergeKLists(input);

    // cast output from ListNode to ArrayList for easy comparison
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
    // initialize input, expected output, and actual output 
    ListNode[] input = new ListNode[3];
    input[0] = new ListNode(1, new ListNode(4, new ListNode(5, null)));
    input[1] = new ListNode(1, new ListNode(3, new ListNode(4, null)));
    input[2] = new ListNode(2, new ListNode(6, null));
    ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(1,1,2,3,4,4,5,6));
    ListNode output = MergeKSortedLists.mergeKLists(input);

    // cast output from ListNode to ArrayList for easy comparison
    ArrayList<Integer> actual = new ArrayList<>();
    for (ListNode temp = output; temp != null; temp = temp.next){
      actual.add(temp.val);
    }

    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected.equals(actual));
  }

}
