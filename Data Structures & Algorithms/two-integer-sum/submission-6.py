class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,j in range(len(nums)):
            if nums[i] == nums[i-1]:
                return True
            return False

