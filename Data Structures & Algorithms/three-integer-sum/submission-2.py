class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        i,j,k = 0, 1, len(nums) - 1
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                j = i + 1
                k = len(nums) - 1
                continue
            target = -nums[i]
            while j < k:
                total = nums[j] + nums[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    results.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1
                    k -= 1
            i += 1
            j = i + 1
            k = len(nums) - 1
        return results
