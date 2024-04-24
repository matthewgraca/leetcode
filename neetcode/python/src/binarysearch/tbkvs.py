class TimeMap:
    '''
    Key maps to a list of pairs, containing a timestamp and corresponding value
    timemap = {key, [(timestamp, value)]}
    '''
    def __init__(self):
        self.timemap = {}

    '''
    Stores the key with the value at a given timestamp
    '''
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [(timestamp, value)]
        else:
            self.timemap[key].append((timestamp, value))
        '''
        original code:

        self.timemap[key] = self.timemap.get(key, []) + [(timestamp, value)]

        apparently this is enough to 10x the run time of the tests.

        The reason why is becase "+" and "append" do different things.
        - append simply adds the list onto the other list (as a reference)
        - + takes the two lists and generates a new list containing both

        The result is quite insane.
        - "append" has O(1) addition, or O(n) for n items
        - "+" has O(n) addition; since you're making a new list out of the previous 
            lists, it looks like: 1+2+3+4+5 ... n, for n(n-1)/2 or O(n^2) to add n items
        '''

    '''
    Returns the value that was previously set, with timestamp_prev <= timestamp.
    If there are multiple such values, return the value with the largest stamp.
    If there are no values, return an empty string.
    '''
    def get(self, key: str, timestamp: int) -> str:
        # check if the key exists
        if key not in self.timemap:
            return ""

        # if the timestamp is smaller than all, there is no valid value
        firstValue = self.timemap[key][0][0]
        if timestamp < firstValue:
            return ""

        # if the timestamp is larger than all, the top value is the value
        lastValue = self.timemap[key][-1][0]
        if timestamp > lastValue:
            return self.timemap[key][-1][1]

        # binary search for key timestamp
        n = len(self.timemap[key])
        lower, upper = 0, n-1
        while lower <= upper:
            mid = (upper + lower) // 2
            midTimestamp = self.timemap[key][mid][0]
            if timestamp < midTimestamp:
                upper = mid-1
            elif timestamp > midTimestamp:
                lower = mid+1
            else:
                return self.timemap[key][mid][1]

        # value not found; the timestamp is somewhere in the middle.
        # return the value with a timestamp smaller but closest to it
        return self.timemap[key][mid-1][1]
