class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l != r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]: #left portion, everything before mid is less than
                l = mid + 1
            else: # nums[mid] < nums[r] right portion, everything after mid is greater
                r = mid
        return nums[l]