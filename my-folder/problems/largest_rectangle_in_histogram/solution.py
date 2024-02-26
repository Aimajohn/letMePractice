class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxSq = [], 0

        for i, n in enumerate(heights):
            start = i
            while stack and stack[-1][1] > n:
                previ, alt = stack.pop()
                maxSq = max(maxSq, (i-previ)*alt)
                start = previ

            stack.append([start, n])
        
        for index, alt in stack:
            maxSq = max(maxSq, (len(heights)-index)*alt)

        return maxSq