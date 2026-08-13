class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        m = dict()
        for num in nums:
            m[num] = 0
        for num in nums:
            temp = 0
            if num - 1 not in m:
                temp += 1
                while num + 1 in m:
                    temp += 1
                    num += 1
                if temp > count:
                    count = temp
        return count
        


        