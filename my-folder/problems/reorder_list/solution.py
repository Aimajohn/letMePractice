# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mah = curr = head
        nea = []
        
        while head:
            head = head.next
            nea.append(head)
        ab = len(nea)
        if ab <=2:
            return mah
            
        nea[len(nea)//2-1].next = nea.pop()

        for i in range(0,ab//2):
            nea[-i-1].next, curr.next = curr.next, nea[-i-1]
            curr = nea[-i-1].next
        
        return mah
        
        """
        Do not return anything, modify head in-place instead.
        """