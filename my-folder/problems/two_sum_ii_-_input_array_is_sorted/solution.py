class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        counterL = 0
        counterR = len(numbers)-1
        while counterL < counterR:
            if numbers[counterL]+numbers[counterR] == target:
                return [counterL+1, counterR+1]
            elif numbers[counterL]+numbers[counterR] < target:
                counterL+=1
            else:
                counterR-=1