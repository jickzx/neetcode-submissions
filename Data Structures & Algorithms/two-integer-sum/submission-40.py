class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Pass = {}

        for i,j in enumerate(nums):
            diff = target - j
            if diff in Pass:
                return [Pass[diff], i]
            Pass[j] = i
            