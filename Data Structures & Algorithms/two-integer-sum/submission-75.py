class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,n in enumerate(nums):
            diff = n - target
            if diff in seen:
               return [seen[diff],i]
            seen[n] = i   