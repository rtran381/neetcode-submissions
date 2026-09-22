class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        cur = float('-inf')
        for num in nums:
            if cur < 0:
                cur = 0
            cur += num
            maximum = max(cur, maximum)
        return maximum