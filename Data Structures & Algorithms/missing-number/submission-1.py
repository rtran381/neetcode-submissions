class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = len(nums)
        for num in range(len(nums)):
            i ^= num ^ nums[num] 
        return i