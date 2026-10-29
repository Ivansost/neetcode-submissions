# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        prev = None
        cur = head

        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        head = prev

        count = 1
        prev = None
        cur = head

        

        while count != n:
            prev = cur
            cur = cur.next
            count += 1
    
        if prev == None:
            head = cur.next
        else:
            prev.next = cur.next

        prev = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        head = prev

        return head
        