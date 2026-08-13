class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        m = set(nums)
        for num in m:
            if num - 1 not in m:
                temp = 1
                while num + 1 in m:
                    temp += 1
                    num += 1
                count = max(count, temp)
        return count
        


        