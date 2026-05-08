class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        temp = nums[0]
        for number, i in enumerate(nums[1:]):
            if number == temp:
                return True
            temp = number
        return False

# from typing import List

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))