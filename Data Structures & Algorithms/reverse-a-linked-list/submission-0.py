# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        arr = deque([])
        while head:
            arr.appendleft(head.val)
            head = head.next
        
        node = ListNode()
        dummy = ListNode(next=node)
        while arr:
            val = arr.popleft()
            node.val = val

            if arr:
                next_node = ListNode()
                node.next = next_node
                node = node.next
            
        return dummy.next
