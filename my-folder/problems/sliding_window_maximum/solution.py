from collections import deque
class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxs = []
        temp = deque([])
        for i in range(len(nums)):
            while temp and nums[temp[-1]] < nums[i]:
                temp.pop()
            temp.append(i)
            if i>=k-1:
                if temp[0] == i-k:
                    temp.popleft()
                maxs.append(nums[temp[0]])
        return maxs