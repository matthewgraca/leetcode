package mgraca;

import static org.junit.Assert.*;

import org.junit.Test;

import java.util.ArrayList;
import java.util.Arrays;

public class MergeTwoSortedListsTest{
  @Test
  public void example1(){
    // initialize inputs and expected output
    ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4, null)));
    ListNode l2 = new ListNode(1, new ListNode(3, new ListNode(4, null)));
    ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(1, 1, 2, 3, 4, 4));

    // create output list and convert to an array
    ListNode actualList = MergeTwoSortedLists.mergeTwoLists(l1, l2);
    ArrayList<Integer> actual= new ArrayList<>();
    for (ListNode temp = actualList; temp != null; temp = temp.next){
      actual.add(temp.val);
    }

    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual.equals(expected));
  }

  @Test
  public void example2(){
    ListNode l1 = null;
    ListNode l2 = null;
    ListNode expected = null;
    ListNode actual = MergeTwoSortedLists.mergeTwoLists(l1, l2);
    assertTrue(actual == expected);
  }

  @Test
  public void example3(){
    ListNode l1 = null;
    ListNode l2 = new ListNode(0, null);
    ListNode expected = new ListNode(0, null);

    ListNode actual = MergeTwoSortedLists.mergeTwoLists(l1, l2);
    for (ListNode expectedTemp = expected, actualTemp = actual; 
    expectedTemp != null; 
    expectedTemp = expectedTemp.next, actualTemp = actualTemp.next){
      assertTrue(expectedTemp.val == actualTemp.val);
    }
  }

  @Test
  public void recExample1(){
    // initialize inputs and expected output
    ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4, null)));
    ListNode l2 = new ListNode(1, new ListNode(3, new ListNode(4, null)));
    ArrayList<Integer> expected = new ArrayList<>(Arrays.asList(1, 1, 2, 3, 4, 4));

    // create output list and convert to an array
    ListNode actualList = MergeTwoSortedLists.recMergeTwoLists(l1, l2);
    ArrayList<Integer> actual= new ArrayList<>();
    for (ListNode temp = actualList; temp != null; temp = temp.next){
      actual.add(temp.val);
    }

    // test
    String msg = "Expected " + expected + ", returned " + actual;
    assertTrue(msg, actual.equals(expected));
  }

  @Test
  public void recExample2(){
    ListNode l1 = null;
    ListNode l2 = null;
    ListNode expected = null;
    ListNode actual = MergeTwoSortedLists.recMergeTwoLists(l1, l2);
    assertTrue(actual == expected);
  }

  @Test
  public void recExample3(){
    ListNode l1 = null;
    ListNode l2 = new ListNode(0, null);
    ListNode expected = new ListNode(0, null);

    ListNode actual = MergeTwoSortedLists.recMergeTwoLists(l1, l2);
    for (ListNode expectedTemp = expected, actualTemp = actual; 
    expectedTemp != null; 
    expectedTemp = expectedTemp.next, actualTemp = actualTemp.next){
      assertTrue(expectedTemp.val == actualTemp.val);
    }
  }

}
