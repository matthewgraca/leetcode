package mgraca;

import java.util.PriorityQueue;
import java.util.Collections;

/*
 * Description: You are given an array of k linked-lists, where each 
 *  linked-list is sorted in ascending order. Merge all the linked-lists 
 *  into one ordered linked-list and return it.
 *
 * Constraints:
 *  k == lists.length
 *  0 <= k <= 10^4
 *  0 <= lists[i].length <= 500
 *  -10^4 <= lists[i][j] <= 10^4
 *  lists[i] is sorted in ascending order
 *  The sum of lists[i].length will not exceed 10^4
 *
 * Complexity:
 *  Time: O(nlogn), the cost of adding n items to a priority queue, and 
 *    subsequently removing n items from a priority queue of size n.
 *  Space: O(n), the cost of creating a priority queue of size n and the 
 *    solution list of size n.
 */
public class MergeKSortedLists{
  public static ListNode mergeKLists(ListNode[] lists){
    // guard against empty list
    if (lists == null)
      return null;

    // add all items in the list to a priority queue
    PriorityQueue<Integer> pq = new PriorityQueue<>(11, Collections.reverseOrder());
    for (int i = 0; i < lists.length; i++){
      for (ListNode j = lists[i]; j != null; j = j.next){
        pq.add(j.val);
      }
    }

    // use pq to create solution
    ListNode solution = null;
    while (!pq.isEmpty()){
      ListNode temp = new ListNode(pq.poll(), null);
      temp.next = solution;
      solution = temp;
    }
    return solution;
  }
}
