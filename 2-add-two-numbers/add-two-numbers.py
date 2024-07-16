# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        dummyNode = ListNode(-1)
        curr = dummyNode
        carry = 0
        while temp1 or temp2:
            sum = carry
            if temp1:
                sum = sum + temp1.val
            if temp2:
                sum = sum + temp2.val
            newNode = ListNode(sum % 10)
            carry = sum // 10
            curr.next = newNode
            curr = curr.next

            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        if carry:
            newNode = ListNode(carry)
            curr.next = newNode

        head = dummyNode.next
        return head

        
        

