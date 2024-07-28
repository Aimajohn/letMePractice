# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numbers = ["", ""]
        while l1:
            numbers[0] = str(l1.val) + numbers[0]
            l1 = l1.next
        
        while l2:
            numbers[1] = str(l2.val) + numbers[1]
            l2 = l2.next
        
        temp = str(int(numbers[0])+int(numbers[1]))
        head = 0
        final = 0
        for i in range(len(temp)):
            if head:
                head.next = ListNode(temp[-i-1])
                head = head.next
            else:
                head = ListNode(temp[-1])
                final = head
            
        return final 

