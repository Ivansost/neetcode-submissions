# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fp = head
        sp = head

        #find mid
        while fp and fp.next:

            fp = fp.next.next
            sp = sp.next

        #reverse
        prev = None
        cur = sp.next
        sp.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        #merge
        
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2