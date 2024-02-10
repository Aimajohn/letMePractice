class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        onList = set()
        for num in nums:
            if(num in onList):
                return True
            onList.add(num)
        return False