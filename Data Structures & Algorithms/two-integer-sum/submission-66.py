class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map
        seen = {}

        for i,j in enumerate(nums):
            # remember, when doing this, we want to go in 1 pass, making it o(n) time and memory as it depends on how many values there are
            diff = target - j
            if diff in seen:
                return [seen[diff], i]
            seen[j] = i