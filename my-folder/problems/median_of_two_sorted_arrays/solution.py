class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = (len(nums1)+len(nums2))
        last = []
        i,u, j = 0, 0, total/2
        if total%2 == 0 :
            j = total//2+1
        else:
            j = total/2
        while (i + u) < j:
            print(i, u, i < len(nums1))
            if i < len(nums1) and (u >= len(nums2) or nums1[i] <= nums2[u] ) :
                last.append(nums1[i])
                i+=1
            elif u < len(nums2)  :
                last.append(nums2[u])
                u+=1
        print(last) 
        if total%2 == 1:
            return last[-1]
        else:
            return (last[-1]+last[-2])/2
            
            

