class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passs = {} # pass is a function...
        for i,j in enumerate(nums):
            diff = target - j
            if passs in diff:
                return passs[diff], i
            
            passs[j] = i