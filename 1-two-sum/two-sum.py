class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for each number, we check if (target-number) is in the array or not
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                # what if target is 6 and we have 3 --> it will return same indexes twice, so this condition
                if i == nums.index(target-nums[i]):
                    continue
                else:
                    return [i, nums.index(target-nums[i])]
        
