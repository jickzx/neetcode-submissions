class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # hashmap so value : index

        for i,j in enumerate(nums):
            if nums[i] + nums[j] == target and nums[i] != nums[j]:
                seen = seen[nums[i]]
        return seen