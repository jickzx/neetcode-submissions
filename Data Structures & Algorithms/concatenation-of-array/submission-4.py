class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2): # repeat twice
            for num in nums:
                ans.append(num)
        return ans
        # i had the answer in my face this entire time are you kidding me