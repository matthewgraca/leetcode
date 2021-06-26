package mgraca.medium;

/*
 * Description: You are given two non-empty linked lists representing two non-negative integers. 
 *  The digits are stored in reverse order, and each of their nodes contains a single digit. 
 *  Add the two numbers and return the sum as a linked list.
 *
 *  You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * 
 * Constraints:
 *  The number of nodes in each linked list is in the range [1, 100].
 *  0 <= Node.val <= 9
 *  It is guaranteed that the list represents a number that does not have leading zeros.
 */
public class AddTwoNumbers{
  public static ListNode addTwoNumbers(ListNode l1, ListNode l2){
    ListNode sol = null;
    ListNode temp1 = l1;
    ListNode temp2 = l2;
    int localSum = 0;
    boolean carry = false;

    // initialize
    localSum = temp1.val + temp2.val;
    if (localSum >= 10){
      localSum -= 10;
      carry = true;
    }
    sol = new ListNode(localSum);
    ListNode temp = sol;
    temp1 = temp1.next;
    temp2 = temp2.next;

    // traverse lists
    while (temp1 != null || temp2 != null){
      // initialize proper sum
      if (temp1 == null){
        localSum = temp2.val;
        temp2 = temp2.next;
      }
      else if (temp2 == null){
        localSum = temp1.val;
        temp1 = temp1.next;
      }
      else{
        localSum = temp1.val + temp2.val;
        temp1 = temp1.next;
        temp2 = temp2.next;
      }

      // determine if carry should apply
      if (carry){
        localSum++;
        carry = false;
      }

      if (localSum >= 10){
        localSum -= 10;
        carry = true;
      }

      // push to solution list
      temp.next = new ListNode(localSum);
      temp = temp.next;
    }

    // handle leftover carry if it exists
    if (carry){
      temp.next = new ListNode(1);
    }
    return sol;
  }
}
