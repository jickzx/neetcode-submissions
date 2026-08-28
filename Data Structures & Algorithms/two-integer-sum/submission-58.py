class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force method

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return nums[i]
                nums[j] = i