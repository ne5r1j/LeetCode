class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_of_elements = 0
        sum_of_digits = 0
        for i in nums:
            sum_of_elements += i
            sum = 0
            while i != 0:
                x = i % 10
                sum += x
                i = i // 10
            sum_of_digits += sum
        
        return (sum_of_elements - sum_of_digits) if sum_of_elements > sum_of_digits else sum_of_digits- sum_of_elements


