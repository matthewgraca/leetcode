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
 *  Time:   O(n), where n is the number of nodes in the list. We need to 
 *    find the end of the list to know where we should place our pointer 
 *    that removes the node we are looking for.
 *  Space:  O(1), we are only using two pointers no matter the list size.
 */
public class RemoveNthNodeFromEndOfList{
  public static ListNode removeNthFromEnd(ListNode head, int n){
    // set up 2 pointers; one that removes and one that searches
    ListNode root = head;
    ListNode search = head;
    boolean endFound = false;

    // edge cases - 1 node; n guaranteed to be 1 by problem
    if (head.next == null){
      return null;
    }

    // move the search pointer up depending on how far n is
    for (int i = 0; i <= n; i++){
      // implies n == sz and head is to be removed
      if (search == null){
        endFound = true;
        head = head.next;
        break;
      }
      else
        search = search.next;
    }

    // when the end is reached, root.next is the nth node; remove it
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
