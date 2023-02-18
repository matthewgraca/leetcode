package mgraca.hard;

import mgraca.ListNode;

/*
 * Description: Given the head of a linked list, reverse the nodes of the list 
 *  k at a time, and return the modified list. k is a positive integer and is 
 *  less than or equal to the length of the linked llist. If the number of 
 *  nodes is not a multiple of k then left-out nodes, in the end, should 
 *  remain as it is. You may not alter the values in the list's nodes, only 
 *  the nodes themselves may be changed.
 *
 * Follow-up: Can you solve the problem in O(1) space?
 *
 * Constraints:
 *  The number of nodes in the list is n
 *  1 <= k <= n <= 5000
 *  0 <= Node.val <= 1000
 *
 * Complexity:
 *  Time:
 *  Space:
 */
public class ReverseNodesInKGroup{
  public static ListNode reverseKGroup(ListNode head, int k){
    // base case: no node remains or less than k nodes remain
    if (head == null || head.next == null)
      return head;

    // swap node pair
    ListNode node = head.next;
    head.next = node.next;
    node.next = head;
    head.next = reverseKGroup(head.next);


    // reverse list up to k nodes
    ListNode node = reverseKGroup(head.next, k-1);
    return node;
  }
}
