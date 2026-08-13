class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        i,j,k = 0, 1, len(nums) - 1 # i is outer loop, j is left pointer, k is right pointer
        
        while i < len(nums) - 2:
            if nums[i] > 0 or i > 0 and nums[i] == nums[i-1]: # if i is same number as previously, increment
                i += 1
                j = i + 1
                k = len(nums) - 1
                continue
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0: # increment left pointer if less than zero
                    j += 1
                elif total > 0: #increment right pointer if greater than zero
                    k -= 1
                else: # = 0
                    results.append([nums[i],nums[j],nums[k]])
                    j += 1 #increment to not get dupe 
                    k -= 1 #decrement to not get dupe          
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
            i += 1
            j = i + 1
            k = len(nums) - 1
        return results
