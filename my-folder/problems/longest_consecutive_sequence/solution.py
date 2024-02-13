class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res= 0
        cdict = set(nums)
        for i in cdict:
            if i-1 not in cdict:
                count = 1
                while i+count in cdict:
                    count+=1
                res = max(res, count)
        return res
        