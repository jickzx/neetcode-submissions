class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = {}
        # for i,j in enumerate(nums):
        #     diff = target - j
        #     if diff in seen:
        #         return [seen[diff],i]
        #     seen[j] = i

        # Faster method:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and nums[i] != nums[j]:
                    return i, j