from typing import List

class Solution:
    def carFleet(target: int, position: List[int], speed: List[int]) -> int:
        # map the position and car as a pair, then sort by position 
        positionStack = sorted((pos,car) for car, pos in enumerate(position))

        # check the time it takes for the top car to finish the race
        # if this time is faster than the car in front, then merge as one fleet
        fleets = 0
        currentTime = 0
        while positionStack:
            pos, car = positionStack.pop()
            timeToReachTarget = (target - pos) / speed[car]
            # if the current car is slower, it will be a part of a different fleet
            # if it matches/beats the front car time, it'll be in the same fleet
            if timeToReachTarget > currentTime:
                fleets += 1
                currentTime = timeToReachTarget 
        return fleets
'''
ass problem.
the trick is to sort by position and think of it as a race
if the current car has a worse time, it won't be in the same fleet
    that is, it will be its own fleet; now this time will be the determining time to be in this car's fleet
if the current car can match/beat the next car's time across the finish line, they're in the same fleet
    no updating required
time: nlogn for sort, n to pop - total nlogn
space: n for stack
'''
