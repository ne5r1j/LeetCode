# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        temp = head
        while temp:
            list1.append(temp.val)
            temp = temp.next

        list1.sort()

        temp = head
        i = 0
        while temp:
            temp.val = list1[i]
            i += 1
            temp = temp.next

        return head

        