class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for i in range(2): # repeat twice
                for num in nums:
                    ans.append(nums)
            combined = ans[nums] + ans[nums]
            # fuck.
                