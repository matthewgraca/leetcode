from typing import List

class Solution:
    def carFleet(target: int, position: List[int], speed: List[int]) -> int:
        # map each car to their position, then sort by position
        # such that the top of the stack contains the car closest to the finish
        sortedPosition = sorted((pos, car) for (car, pos) in enumerate(position))
        fleets, timeToBeat = 0, 0

        while sortedPosition:
            # calculate the time it takes for the foremost car to finish the race
            pos, car = sortedPosition.pop()
            timeToFinish = (target - pos) / speed[car]

            # if can't catch the front car, add a fleet
            # and, it'll be the new "time to beat" for the next car 
            if timeToFinish > timeToBeat:
                fleets += 1
                timeToBeat = timeToFinish

        return fleets
