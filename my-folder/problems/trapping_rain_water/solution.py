class Solution:
    def trap(self, height: List[int]) -> int:
        awa, i, j = 0, 0, 1
        k = max(height)
        tempAwa, tempNeg = 0,0
        tempH, tempNH = 0, 0
        passed = False
        while i < len(height)-1:
            if height[j]<height[i] or tempH>height[j]:
                if height[i] > tempH:
                    tempH = height[i]
                tempAwa += tempH-height[j]
            elif height[j]>height[i]:
                awa+=tempAwa
                tempAwa = 0
                tempH = height[j]
            if height[-i-1] == k:
                passed = True
            if not passed:
                tempNH = max(height[-i-1], tempNH)
                tempNeg += k-tempNH
            j+=1
            i+=1
        awa=awa+tempAwa-tempNeg
        return awa