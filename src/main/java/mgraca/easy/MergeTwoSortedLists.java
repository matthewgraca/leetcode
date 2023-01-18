package mgraca.easy;

import mgraca.ListNode;

/*
 * Description: You are given the heads of two sorted linked lists `list1` 
 *  and `list2`. Merge the two lists in a one sorted list. The list should 
 *  be made by splicing together the nodes of the first two lists. Return 
 *  the head of the merged linked list.
 *
 * Constraints:
 *  The number of nodes in both lists is in the range [0, 50]
 *  -100 <= Node.val <= 100
 *  Both list1 and list2 are sorted in non-decreasing order
 *
 * Complexity:
 *  Time:   O(n), where n is the sum of the size of both lists. Worst case is 
 *    both lists have values that weave together, so we increment through every 
 *    node.
 *  Space:  O(1), no matter the size of each list we'll have the same number of 
 *    temp nodes to track and merge.
 */
public class MergeTwoSortedLists{
  public static ListNode mergeTwoLists(ListNode list1, ListNode list2){
    ListNode temp1 = list1;
    ListNode temp2 = list2;
    ListNode temp3 = null;
    if (temp1 == null)  // if list1 is empty, then list2 is the merged order 
      return temp2;
    if (temp2 == null)  // if list2 is empty, then list1 is the merged order
      return temp1;

    // otherwise, list1 and list2 have values and need to be merged
    // let temp3 be the smallest value of both lists
    if (temp1.val < temp2.val){
      temp3 = temp1;
      temp1 = temp1.next;
    }
    else{
      temp3 = temp2;
      temp2 = temp2.next;
    }
    ListNode head = temp3;

    // check the next node of each list. smaller gets attached to temp3
    // continue until one of 3 conditions are met
    // 1. both lists are empty
    while (temp1 != null || temp2 != null){
      // 2. temp1 empties first, pull rest from temp2
      if (temp1 == null){
        temp3.next = temp2;
        break;
      }
      // 3. temp2 empties first, pull rest from temp1
      if (temp2 == null){
        temp3.next = temp1;
        break;
      }
      // compare this val with l1 and l2
      // if l1 val is smaller, connect to l1; else connect to l2
      if (temp1.val < temp2.val){
        temp3.next = temp1;
        temp1 = temp1.next;
      }
      else{
        temp3.next = temp2;
        temp2 = temp2.next;
      }
      temp3 = temp3.next;
    }
    return head;
  }

  // recursive version of the solution
  public static ListNode recMergeTwoLists(ListNode list1, ListNode list2){
    // base case
    if (list1 == null)  // if list1 is empty, then list2 is the merged order 
      return list2;
    if (list2 == null)  // if list2 is empty, then list1 is the merged order
      return list1;

    // check order
    if (list1.val < list2.val){
      list1.next = recMergeTwoLists(list1.next, list2);
      return list1;
    }
    else{
      list2.next = recMergeTwoLists(list1, list2.next);
      return list2;
    }
  }
}
