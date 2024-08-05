class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = []
        for i in s:
            if i.isalnum():
                list1.append(i.lower())
        if list1 == list1[::-1]:
            return True
        else:
            return False
        