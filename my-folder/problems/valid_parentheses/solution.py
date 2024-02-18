from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        posibles = {"(": ")", "{":"}", "[": "]"}
        accum = deque([])
        for i, n in enumerate(s):
            if n in posibles:
                accum.append(n)
            elif not accum:
                return False
            else:
                if posibles[accum[-1]] != n:
                    return False
                accum.pop()
        return len(accum) == 0
