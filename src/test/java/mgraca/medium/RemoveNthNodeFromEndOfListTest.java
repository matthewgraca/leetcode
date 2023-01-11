package mgraca.medium;

import static org.junit.Assert.assertTrue;

import org.junit.Test;
import java.util.ArrayList;

public class RemoveNthNodeFromEndOfListTest{
  @Test
  public void example1(){
    // initialize solution
    ArrayList<Integer> al = new ArrayList<>();
    al.add(1);
    al.add(2);
    al.add(3);
    al.add(5);

    // initialize problem
    ListNode temp = new ListNode(1, null);
    ListNode head = temp;
    for (int i = 2; i <= 5; i++){
      temp.next = new ListNode(i, null);
      temp = temp.next;
    }

    // run solution
    ListNode sol = RemoveNthNodeFromEndOfList.removeNthFromEnd(head, 2);

    // check solution
    int i = 0;
    for (ListNode node = sol; node != null; node = node.next){
      String msg = "Expected " + al.get(i) + ", returned " + node.val;
      assertTrue(msg, node.val == al.get(i));
      i++;
    }
  }

  @Test
  public void example2(){
    ListNode head = new ListNode(1, null);
    ListNode actual = null;
    ListNode sol = RemoveNthNodeFromEndOfList.removeNthFromEnd(head, 1);
    assertTrue(sol == actual);
  }

  @Test
  public void example3(){
    // initialize solution
    ArrayList<Integer> al = new ArrayList<>();
    al.add(1);

    // initialize problem
    ListNode head = new ListNode(1, new ListNode(2, null));

    // run solution
    ListNode sol = RemoveNthNodeFromEndOfList.removeNthFromEnd(head, 1);

    // check solution
    int i = 0;
    for (ListNode node = sol; node != null; node = node.next){
      String msg = "Expected " + al.get(i) + ", returned " + node.val;
      assertTrue(msg, node.val == al.get(i));
      i++;
    }
  }

  @Test
  public void example4(){
    // initialize solution
    ArrayList<Integer> al = new ArrayList<>();
    al.add(2);

    // initialize problem
    ListNode head = new ListNode(1, new ListNode(2, null));

    // run solution
    ListNode sol = RemoveNthNodeFromEndOfList.removeNthFromEnd(head, 2);

    // check solution
    int i = 0;
    for (ListNode node = sol; node != null; node = node.next){
      String msg = "Expected " + al.get(i) + ", returned " + node.val;
      assertTrue(msg, node.val == al.get(i));
      i++;
    }
  }

}
