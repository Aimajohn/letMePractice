from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque([])
        sol = deque([])
        for i in range(-1, -len(temperatures)-1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                sol.appendleft(-i+stack[-1])
            else:
                sol.appendleft(0)
            stack.append(i)
        return sol

            