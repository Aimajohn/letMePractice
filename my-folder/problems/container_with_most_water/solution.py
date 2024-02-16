class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxt = 0
        i = 0
        j = len(height)-1
        while i < j:
            h, w = 0, j-i
            if height[i]<height[j]:
                h = height[i]
                i+=1
            else :
                h = height[j]
                j-=1
            maxt = max(maxt, h*w) 
        return maxt