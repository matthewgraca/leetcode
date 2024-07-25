from typing import List

class Solution:
    def __init__(self):
        pass

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # courses from [0, numCourses-1] given a mapping
        prereqMap = {}
        for i in range(numCourses):
            prereqMap[i] = []
        # map prerequisites to each course, {prereq : [courses]}
        for course, prereq in prerequisites:
            prereqMap[prereq].append(course)

        # run dfs on each course
        for course in prereqMap:
            if not self.dfs(prereqMap, course, set()):
                return False

        return True

    def dfs(self, prereqMap: dict, course: int, visited: set) -> bool:
        # leaf hit; backtrack
        if course == []:
            return True
        # cycle found; return False
        if course in visited:
            return False

        visited.add(course)
        children = prereqMap[course]
        for childCourse in children:
            if not self.dfs(prereqMap, childCourse, visited):
                return False
        # valid path found
        # remove path; we already know it's valid, avoid traversing again
        visited.remove(course)
        prereqMap[course] = [] 

        return True

'''
traversing an adjacency list problem


if numCourses < len of the set of classes:
    return False

[a, b] -> course a requires course b

2 things:
    cycle detection for matrix?
    num of courses < len of set of classes

consider a map?
    - problem 1:
        0 -> 1
    -problem 2:
        0 -> 1
        1 -> 0

what if we put all prereqs into a map;
then for each key we follow the path, puttiing the visited nodes
in a set -- if we collide, then there's a cycle?
    - a node may map to more than one value; so if a path is valid, 
        we would still have to backtrack to consider the children

steps:
    1. put prereqs on a map, where b : a (b the preqreq of a)
    1a. (if len of map is larger than num of courses, do we return False?)
        -- alternatively, if we ever "visited more than numCourses nodes", we can return False*
    1b. courses that don't have prereqs aren't a key in the map
    2. dfs on each node. if it ever creates a cycle (node already visited), return False
        -* done here
    3. if no cycle, backtrack to whereever a branch occurred and dfs that
    4. if no cycles, return True

O(n) time yeah
'''
