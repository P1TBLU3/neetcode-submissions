# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        pointer = ListNode()
        current = pointer
        carry = 0

        while l1 or l2 or carry:
            if l1:
                value_1 = l1.val
            else:
                value_1 = 0
            if l2:
                value_2 = l2.val
            else:
                value_2 = 0

            sum = value_1 + value_2 + carry
            carry = int(sum / 10)
            sum = sum % 10
            current.next = ListNode()
            current = current.next
            current.val = sum
            

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

                
        return pointer.next








