# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        current = merged_list

        if not list1 and not list2:
            return None

        val_1 = None
        val_2 = None

        while list1 or list2:
            if list1:
                val_1 = list1.val

            if list2:
                val_2 = list2.val

            if val_1 != None and val_2 != None:
                if val_1 < val_2:
                    current.val = val_1
                    val_1 = None
                    list1 = list1.next
                else:
                    current.val = val_2
                    val_2 = None
                    list2 = list2.next
            elif val_1 == None and val_2 != None:
                current.val = val_2
                val_2 = None
                list2 = list2.next
            elif val_1 != None and val_2 == None:
                current.val = val_1
                val_1 = None
                list1 = list1.next
            else:
                break

            if list1 or list2:
                new_node = ListNode()
                current.next = new_node
                current = current.next
        return merged_list