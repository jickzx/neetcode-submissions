class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for _ in range(len(nums)):
            if nums[i] + nums[j] == nums[i] and nums[i] != nums[j]:
                seen[nums[i]] = nums[i+1]
            return nums[i]