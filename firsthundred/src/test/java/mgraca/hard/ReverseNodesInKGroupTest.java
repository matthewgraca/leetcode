package mgraca.hard;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;
import mgraca.ListNode;

public class ReverseNodesInKGroupTest{
  @Test
  public void example1(){
    // initialize input and output
    ListNode inputList =  new ListNode(1, new ListNode
                                  (2, new ListNode
                                  (3, new ListNode
                                  (4, new ListNode
                                  (5, null)))));
    int k = 2;
    ListNode output = ReverseNodesInKGroup.reverseKGroup(inputList, k);

    // cast actual to arraylist for easy comparison
    ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(2,1,4,3,5));
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
    ListNode inputList =  new ListNode(1, new ListNode
                                  (2, new ListNode
                                  (3, new ListNode
                                  (4, new ListNode
                                  (5, null)))));
    int k = 3;
    ListNode output = ReverseNodesInKGroup.reverseKGroup(inputList, k);

    // cast actual to arraylist for easy comparison
    ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(3,2,1,4,5));
    ArrayList<Integer> actual = new ArrayList<>();
    for (ListNode temp = output; temp != null; temp = temp.next){
      actual.add(temp.val);
    }

    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, expected.equals(actual));
  }
}
