from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        completed = []
        def infinite (i, j, s): 
            if len(s) == n*2 > 0:
                completed.append(s)
            if i < n:
                infinite(i+1, j, s+"(")
            
            if j < i:
                infinite(i, j+1, s+")")
        infinite(0,0,"")
        return completed
            