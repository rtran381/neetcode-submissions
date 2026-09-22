class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        cur = float('-inf')
        for num in nums:
            if num > (cur + num):
                cur = num
            else:
                cur += num
            maximum = max(cur, maximum)
        return maximum