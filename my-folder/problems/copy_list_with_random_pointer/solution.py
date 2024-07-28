"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        head2 = head
        entregable = Node(head.val)
        final = entregable
        notsure = []

        while head2 :
            if head2.next :
                final.next = Node(head2.next.val) 
            temp = head2.next
            head2.next = final
            notsure.append([final, head2])
            final = final.next
            head2 = temp
        
        for a in notsure:
            if a[1].random:
                a[0].random = a[1].random.next


        return entregable