from heapq import *
from typing import List
from collections import deque

class Solution:
    def __init__(self):
        pass

    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = self.frequencyMap(tasks)
        tasksPriorityQueue = [-count for count in taskFreq.values()]
        heapify(tasksPriorityQueue)
        tasksInProgress = deque() # queue contains pairs (-count, idleTime)

        # while (tasks in progress) or (tasks still need to be scheduled)
        time = 0
        while tasksInProgress or tasksPriorityQueue:
            time += 1

            # schedule the task at the top of the pq
            if tasksPriorityQueue:
                tasksRemaining = 1 + heappop(tasksPriorityQueue)
                if tasksRemaining:
                    tasksInProgress.append((tasksRemaining, time + n))
            else: 
                # if no tasks remain to be scheduled,
                # just update time from the task in progress
                time = tasksInProgress[0][1]

            # if there are tasks in progress and their idle time is up,
            # remove from the tasks in progress and place return it to the pq
            if tasksInProgress and tasksInProgress[0][1] == time:
                taskFinished = tasksInProgress.popleft()[0]
                heappush(tasksPriorityQueue, taskFinished)

        return time

    # creates a map counting the frequency of each distinct item in a given list
    def frequencyMap(self, items: list) -> dict:
        freqMap = {}
        for item in items:
            freqMap[item] = freqMap.get(item, 0) + 1
        return freqMap

'''
gonna need to watch the vid on this one
time: 
    - n time to create the frequency map
    - n time to heapify the frequency map
    - for each task, it's bounded by time t worst case; (all n tasks are the same)
        - so the while loop can go for n*t
    - total: nt + n + n := O(nt), where n is the size of the list and t is the length of time
space:
    - n space to make the frequency map
    - n space to make the pq
    - the queue could take up to n items
    - total: n + n + n := O(n)
'''
