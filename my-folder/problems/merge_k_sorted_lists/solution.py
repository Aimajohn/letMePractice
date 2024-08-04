# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) <=1:
            if len(lists) ==1:
                return lists[0]
            return
        total = []
        for list in lists:
            while list:
                total.append(list.val)
                list = list.next
        if len(total) == 0:
            return 
        total.sort()
        head = ListNode(total[0])
        ent = head
        for item in total[1:]:
            head.next = ListNode(item)
            head = head.next
        return ent
