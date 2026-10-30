# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        values = []

        for i in range(len(lists)):
            head = lists[i]

            while head:
                values.append(head.val)
                head = head.next

        values.sort()
        new = ListNode()
        head = new

        for i in range(len(values)):

            head.next = ListNode(values[i])
            head = head.next

        head = new.next

        return head
