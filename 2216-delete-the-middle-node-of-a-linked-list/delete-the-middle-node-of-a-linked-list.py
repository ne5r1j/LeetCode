# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        if length == 1:
            head = None
            return head
        if length // 2 == 0:
            index = length // 2 + 1
        else:
            index = length // 2
        
        temp = head
        for _ in range(index - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head
        