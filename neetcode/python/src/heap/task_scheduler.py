import heapq
from typing import List
from collections import deque

class Solution:
    def __init__(self):
        pass
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskFreq = self.frequencyMap(tasks)
        tasksPriorityQueue = [-count for count in taskFreq.values()]
        heapq.heapify(tasksPriorityQueue)
        tasksInProgress = deque() # queue contains pairs (-count, taskFinishTime)

        # while (tasks in progress) or (tasks still need to be scheduled)
        time = 0
        while tasksInProgress or tasksPriorityQueue:
            time += 1

            # if there is a task to schedule, put it in the queue.
            if tasksPriorityQueue:
                tasksRemaining = 1 + heapq.heappop(tasksPriorityQueue)
                if tasksRemaining:
                    tasksInProgress.append((tasksRemaining, time + n))
            # if no tasks remain to be scheduled,
            else: 
                # just update time from the task in progress
                time = tasksInProgress[0][1]

            # if the task in progress is completed,
            # remove it from the queue and place return it to the pq
            if tasksInProgress and tasksInProgress[0][1] == time:
                taskFinished = tasksInProgress.popleft()[0]
                heapq.heappush(tasksPriorityQueue, taskFinished)

        return time

    # creates a map counting the frequency of each distinct item in a given list
    def frequencyMap(self, items: list) -> dict:
        freqMap = {}
        for item in items:
            freqMap[item] = freqMap.get(item, 0) + 1
        return freqMap
