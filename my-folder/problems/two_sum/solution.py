class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        usefulNumbers = {}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if(complement in usefulNumbers):
                return [usefulNumbers[complement], i]
            usefulNumbers[nums[i]] = i
        return []

                

