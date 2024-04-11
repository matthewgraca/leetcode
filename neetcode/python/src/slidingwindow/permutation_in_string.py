class Solution:
    def checkInclusion(s1: str, s2: str) -> bool:
        left = 0
        freqs1 = dict()
        freqs2 = dict()
        windowLen = len(s1)

        # frequency map for s1
        for a in s1:
            freqs1[a] = freqs1.get(a, 0) + 1

        for right in range(len(s2)):
            # frequency map for the window in s2
            freqs2[s2[right]] = freqs2.get(s2[right], 0) + 1
            # initializes window
            if right-left+1 < windowLen:
                continue 
            else:
                # search for valid anagram(permutation)
                if freqs1 == freqs2:
                    return True
                else:
                    # move left pointer, remove from map if count goes to 0
                    if freqs2[s2[left]] == 1:
                        freqs2.pop(s2[left])
                    else:
                        freqs2[s2[left]] -= 1
                    left += 1
        return False
