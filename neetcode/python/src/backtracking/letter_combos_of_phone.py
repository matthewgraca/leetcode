from typing import List

class Solution:
    def __init__(self):
        pass

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        self.checkNode(0, digits, self.numberToLettersMap(), [], res)
        return res

    def checkNode(
        self,
        i: int,
        digits: str,
        numberToLettersMap: dict,
        combo: List[str],
        res: List[str]
    ) -> None:
        # base case 1: no digits
        if not digits:
            return
        # base case 2: solution found, digits scan is finished
        if i == len(digits):
            res.append(''.join(combo))
            return

        # traverse through all letters (children) for a given number (parent)
        letters = numberToLettersMap[int(digits[i])]
        for letter in letters:
            combo.append(letter)
            self.checkNode(i + 1, digits, numberToLettersMap, combo, res)
            combo.pop()

        # all letters checked; backtrack to prev letter
        return

    def numberToLettersMap(self) -> dict:
        d = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        return d
