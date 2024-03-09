from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nlist = None
        actual = head
        while actual:
            temp = actual.next
            actual.next = nlist
            nlist = actual
            actual = temp
        return nlist
