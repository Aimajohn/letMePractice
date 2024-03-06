
def binary(snums, target, k):
    i,j = 0, len(snums)-1
    
    while i<=j:
        val = j+i//2
        if  snums[val]  == target:
            return val+k
        elif snums[val] < target:
            i = val+1
        else:
            j = val-1
    return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        if nums[0] == target:
            return 0
        if nums[0] <= nums[-1]:
            return binary(nums, target, i)
        else:
            snums = nums
            for i in range(1, len(nums)):
                if nums[i] == target:
                    return i
                if nums[i] <= nums[i-1]:
                    snums = nums[i:]
                    break
                
            return binary(snums, target, i)
