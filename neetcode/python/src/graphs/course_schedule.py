from typing import List

class Solution:
    def __init__(self):
        pass

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # courses from [0, numCourses-1] given a mapping
        # map prerequisites to each course, {prereq : [courses]}
        prereqMap = {i : [] for i in range(numCourses)}
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
