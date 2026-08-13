class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        ret = [1] * length

        pre = 1
        for i in range(length):
            ret[i] = pre
            pre *= nums[i]

        suff = 1

        for i in range(length - 1, -1, -1):
            ret[i] *= suff
            suff *= nums[i]

        return ret
