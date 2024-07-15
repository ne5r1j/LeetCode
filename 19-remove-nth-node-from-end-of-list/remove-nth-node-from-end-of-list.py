# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        if length == n:
            newHead = head.next
            return newHead
        
        index = length - n
        temp = head

        while temp:
            index -= 1
            if index == 0:
                break
            temp = temp.next
        
        delete_node = temp.next
        temp.next = temp.next.next

        return head

            

        # if length == 1:
        #     head.next = None
        #     return head
        # for _ in range(index):
        #     temp = temp.next
        # if n == 1:
        #     temp.next = None
        # else:
        #     temp.next = temp.next.next
        # return head