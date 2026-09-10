class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        # want to do everything in 1 pass so we dont need n^2

        for i,j in enumerate(nums):
            diff = target - j
            if seen in diff:
                return [seen[diff],i]
            
            seen[j] = i