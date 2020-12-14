class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            if (target - num in nums) and (index != nums.index(target - num)):
                return index, nums.index(target - num)


