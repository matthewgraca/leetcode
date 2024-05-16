class TimeMap:
    '''
        Let timemap = {key, [(timestamp, value)]}, a map that associates
        a key with a list of timestamp and value pairs.
    '''
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [(timestamp, value)]
        else:
            self.timemap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        # case 1: key dne; return empty string
        if key not in self.timemap:
            return ""
        
        # values = [(timestamp, value)]
        values = self.timemap[key]
        # case 2: timestamp below lower bound; return empty string
        if timestamp < values[0][0]:
            return ""
        
        # case 3: timestamp above upper bound; return supremum
        if timestamp >= values[-1][0]:
            return values[-1][1]

        # case 4: timestamp contained within boundaries of values
        l, r, mid = 0, len(values)-1, 0
        while l <= r:
            mid = (l + r) // 2
            timestampAtMid, valAtMid = values[mid]
            if timestamp < values[mid][0]:
                r = mid-1
            elif timestamp > values[mid][0]:
                l = mid+1
            else:
                return values[mid][1]
        # timestamp not found; get value with supremum timestamp
        return values[mid-1][1]
