class Solution:
    def minWindow(s: str, t: str) -> str:
        left = 0
        freqt, freqsw = dict(), dict()
        have, need = 0, len(t)
        minWindowLen = float('inf')
        minLeft, minRight = 0, 0

        # generate a frequency map for t
        for a in t:
            freqt[a] = freqt.get(a,0) + 1

        for right in range(len(s)):
            # if this value is what we "need", update what we "have"
            freqsw[s[right]] = freqsw.get(s[right],0) + 1
            if s[right] in freqt and freqsw[s[right]] <= freqt[s[right]]:
                have += 1

            # if we "have" all the chars that we "need"
            while have == need:
                # check if this substr changes the min substr size
                windowLen = right - left
                if windowLen < minWindowLen:
                    minWindowLen = windowLen
                    minLeft, minRight = left, right

                # start moving the left ptr to check new substr
                freqsw[s[left]] -= 1
                # update how this impacts what you "have"
                if s[left] in freqt and freqsw[s[left]] < freqt[s[left]]:
                    have -= 1

                left += 1
        return "" if minWindowLen == float('inf') else s[minLeft:minRight+1] 
