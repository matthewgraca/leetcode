from typing import List

class Solution:
    def __init__(self):
        pass


    def findOrder(
        self, 
        numCourses: int, 
        prerequisites: List[List[int]]
    ) -> List[List[int]]:
        # courses from [0, numCourses-1] given a default mapping to empty list
        prereqMap = {i: [] for i in range(numCourses)}
        # this time we map course to their prereqs, {course : [prereqs]}
        # this means the root of each graph is the last course, and the leaf is the first prereq.
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        # run dfs on each course
        res = []
        visited, cycle = set(), set()
        for course in prereqMap:
            if not self.dfs(prereqMap, course, visited, cycle, res):
                return []

        return res 

    def dfs(
        self, 
        prereqMap: dict, 
        course: int, 
        visited: set,   # keeps track of all visited nodes in successful path 
        cycle: set,     # keeps track of nodes in current path
        res: List[int]
    ) -> bool:
        # cycle found; no order possible
        if course in cycle:
            return False
        # ignore paths already visited; we know they're valid
        if course in visited:
            return True

        cycle.add(course)
        children = prereqMap[course]
        for childCourse in children:
            if not self.dfs(prereqMap, childCourse, visited, cycle, res):
                return False
        # valid path found; post-order append to solution and visited set
        # remove path; we already know it's valid, avoid traversing again
        cycle.remove(course)
        visited.add(course)
        res.append(course)

        return True


