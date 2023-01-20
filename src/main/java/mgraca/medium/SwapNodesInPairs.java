package mgraca.medium;

import mgraca.ListNode;

/*
 * Description: Given a linked list, swap eery two adjacent nodes and return 
 *  its head. You must solve the problem without modifying the values in the 
 *  list's nodes (i.e., only nodes themselves may be changed)
 * 
 * Constraints:
 *  The number of nodes in the list is in the range [0,100]
 *  0 <= Node.val <= 100
 *
 * Complexity:
 *  Time:   O(n), since it will need to traverse every element in the list
 *  Space:  O(1), since we do in-place swaps without the creation of an 
 *    auxiliary list
 */
public class SwapNodesInPairs{
  public static ListNode swapPairs(ListNode head){
    // base case: no node remains or one node remains 
    if (head == null || head.next == null)
      return head;

    // swap node pair
    ListNode node = head.next;
    head.next = node.next;
    node.next = head;
    head.next = swapPairs(head.next);
    return node;
  }
}
