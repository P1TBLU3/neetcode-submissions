# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        aux_1 = head
        aux_2 = head.next
        aux_1.next = None

        while aux_2:
            aux_3 = aux_2.next
            aux_2.next = aux_1
            aux_1 = aux_2
            aux_2 = aux_3
        return aux_1