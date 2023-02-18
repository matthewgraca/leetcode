package mgraca.medium;

import static org.junit.Assert.assertTrue;
import org.junit.Test;

import mgraca.ListNode;

public class AddTwoNumbersTest{
  @Test
  public void example1(){
    ListNode l1 = null;
    l1 = new ListNode(3, l1);
    l1 = new ListNode(4, l1);
    l1 = new ListNode(2, l1);
    
    ListNode l2 = null;
    l2 = new ListNode(4, l2);
    l2 = new ListNode(6, l2);
    l2 = new ListNode(5, l2);

    ListNode solution = AddTwoNumbers.addTwoNumbers(l1, l2);

    boolean success = false;
    if (solution.val == 7){
      solution = solution.next;
      if (solution.val == 0){
        solution = solution.next;
        if (solution.val == 8){
          solution = solution.next;
          if (solution == null){
            success = true;
          }
        }
      }
    }
    assertTrue(success);
  }
 
  @Test
  public void example2(){
    ListNode l1 = new ListNode(0);
    ListNode l2 = new ListNode(0);
    ListNode solution = AddTwoNumbers.addTwoNumbers(l1, l2);
    assertTrue(solution.val == 0 && solution.next == null);
  }

  @Test
  public void example3(){
    ListNode l1 = null;
    l1 = new ListNode(9, l1);
    l1 = new ListNode(9, l1);
    l1 = new ListNode(9, l1);
    l1 = new ListNode(9, l1);
    l1 = new ListNode(9, l1);
    l1 = new ListNode(9, l1);
    l1 = new ListNode(9, l1);

    ListNode l2 = null;
    l2 = new ListNode(9, l2);
    l2 = new ListNode(9, l2);
    l2 = new ListNode(9, l2);
    l2 = new ListNode(9, l2);

    ListNode sol = AddTwoNumbers.addTwoNumbers(l1, l2);

    boolean success = false;
    if (sol.val == 8){
      sol = sol.next;
      if (sol.val == 9){
        sol = sol.next;
        if (sol.val == 9){
          sol = sol.next;
          if (sol.val == 9){
            sol = sol.next;
            if (sol.val == 0){
              sol = sol.next;
              if (sol.val == 0){
                sol = sol.next;
                if (sol.val == 0){
                  sol = sol.next;
                  if (sol.val == 1){
                    sol = sol.next;
                    if (sol == null){
                      success = true;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

    assertTrue(success);
  }
}
