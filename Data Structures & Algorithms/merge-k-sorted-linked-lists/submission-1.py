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
        
        while True:
            
            lists = [l for l in lists if l]
            if not lists:
                break
            if len(lists) == 1:
                aux.next = lists[0]
                break

            
            to_add = 10001
            index = 0
            for i in range(len(lists)):
                if lists[i].val < to_add:
                    to_add = lists[i].val
                    index = i

            
            aux.next = lists[index]
            aux = aux.next
            lists[index] = lists[index].next

        return dummy.next
        