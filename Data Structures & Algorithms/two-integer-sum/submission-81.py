class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,j in enumerate(nums):
            diff = target - nums
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[n]=i
