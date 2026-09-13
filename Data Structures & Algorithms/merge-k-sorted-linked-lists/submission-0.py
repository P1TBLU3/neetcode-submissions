# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        dummy = ListNode(0,None)
        aux = dummy
        index = 0
        while len(lists) > 1:
            to_add = 1001
            index = 0
            i = 0
            while i < len(lists):
                if not lists[i]:
                    lists.pop(i)
                else:
                    if lists[i].val < to_add:
                        to_add = lists[i].val
                        index = i
                        
                    i += 1

            aux.next = lists[index]
            aux = aux.next
            lists[index] = lists[index].next
        aux.next = lists[0]
        return dummy.next
        