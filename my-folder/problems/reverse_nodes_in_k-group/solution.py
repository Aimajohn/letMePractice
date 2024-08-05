# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        end = 1
        postit = head
        while head:
            tmp = []
            while len(tmp)< k and head:
                tmp.append(head)
                head = head.next
            if end == 1 and len(tmp) == k:
                end = tmp.pop()
                postit = end
                while len(tmp) != 0:
                    end.next = tmp.pop()
                    end = end.next
            if len(tmp) == k:
                while len(tmp) != 0:
                    end.next = tmp.pop()
                    print(end.next.val)
                    end = end.next
            else:
                for item in tmp:
                    end.next = item
                    end = end.next
        end.next = None
        return postit
