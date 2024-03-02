from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = al = max(piles)
        
        while j-i >= 0:
            val = ceil((j-i)/2) + i
            accum = 0
            for pile in piles:
                accum += ceil(pile/val)
                    
            if accum >= len(piles) and accum <= h and val <= al:
                al = val
            if accum > h:
                i = val+1
            else:
                j = val-1
        
        return al

