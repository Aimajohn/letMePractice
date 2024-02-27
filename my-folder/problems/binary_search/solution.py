class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while   left +1 < right:
            val = (right+left)//2 
            if nums[val] < target:
                left = val
            else:
                right = val

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1