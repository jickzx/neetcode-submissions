class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # index : value (or might be the other way around, forgot but will check later)

        for i,j in enumerate(nums):
            target = hashmap[nums[i]]
            if nums[i] + nums[j] == target:
                return True
            return False