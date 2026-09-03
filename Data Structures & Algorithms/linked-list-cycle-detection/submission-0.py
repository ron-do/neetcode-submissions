# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        addr_set = set()

        while dummy.next:
            dummy = dummy.next
            if id(dummy) in addr_set:
                return True
            
            addr_set.add(id(dummy))

        return False
