class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        common_element = set(set(nums1) & set(nums2))
        out1 = []
        out2 = []
        for i in nums1:
            if i not in common_element and i not in out1:
                out1.append(i)

        
        for i in nums2:
            if i not in common_element and i not in out2:
                out2.append(i)

        return [out1, out2]