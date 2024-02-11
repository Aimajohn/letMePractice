class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        kk = []
        zeros = []
        valor = 1
        for i in range(len(nums)):
            if(nums[i] ==0):
                zeros.append(1)
                kk.append(1)
            else:
                zeros.append(0)
                valor *= nums[i]
                kk.append(nums[i]**-1)
        if sum(zeros) > 1:
            final = [0 for i in range(len(nums))]
        elif sum(zeros) > 0:
            final = [round(kk[i]*valor*zeros[i]) for i in range(len(kk))]
        else:
            final = [round(kk[i]*valor) for i in range(len(kk))]
        return final


            
        