package mgraca.medium;

/*
 * Description: Given the head of a linked list, remove the neth node from 
 *  the end of the list and return its head.
 *
 * Constraints:
 *  The number of nodes in the list is `sz`
 *  1 <= sz <= 30
 *  0 <= Node.val <= 100
 *  1 <= n <= sz
 * 
 * Can this be done in one pass?
 *
 * Complexity:
 *  Time:
 *  Space:
 */
public class RemoveNthNodeFromEndOfList{
  public static ListNode removeNthFromEnd(ListNode head, int n){
    // set up 2 pointers; one that removes and one that searches
    ListNode root = head;
    ListNode search = head;

    // edge cases - 1 node; n guaranteed to be 1 by problem
    if (head.next == null){
      return null;
    }

    // move the search pointer up depending on how far n is
    for (int i = 0; i <= n; i++){
      search = search.next;
    }

    // when the end is reached, root.next is the nth node; remove it
    boolean endFound = false;
    while (!endFound){
      if (search == null){
        root.next = root.next.next;
        endFound = true;
      }
      else{
        root = root.next;
        search = search.next;
      }
    }
    return head;
  }
}
