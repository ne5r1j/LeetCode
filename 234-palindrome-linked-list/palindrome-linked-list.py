# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        check_list = []
        while temp:
            check_list.append(temp.val)
            temp = temp.next
        
        return check_list == check_list[::-1]

        
        