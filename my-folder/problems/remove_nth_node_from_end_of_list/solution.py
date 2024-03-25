# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        foo = 0
        t = curr = k = head
        while t:
            foo+=1
            t = t.next
        i = 0
        if n == foo:
            head = curr = head.next
            i+=1
        if n ==1:
            if foo == 1:
                return 

            while curr:
                if i != foo-n-1:
                    curr = curr.next
                else:
                    curr.next = None
                    curr = curr.next
                i+=1
            return head
                    
        
        i+=1
        curr = curr.next
        while curr:
            if i == foo-n:
                temp = k
                temp.next = curr.next
                curr = curr.next
            else:
                k = k.next
                curr = curr.next
            i+=1
        return head
        print([a.val for a in foo])