class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        i,j,k = 0, 1, len(nums) - 1 # i is outer loop, j is left pointer, k is right pointer
        
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]: # if i is same number as previously, increment
                i += 1
                j = i + 1
                k = len(nums) - 1
                continue
            target = -nums[i]
            while j < k:
                total = nums[j] + nums[k]
                if total < target: # increment left pointer if less than zero
                    j += 1
                elif total > target: #increment right pointer if greater than zero
                    k -= 1
                else: # = 0
                    results.append([nums[i],nums[j],nums[k]])
                    
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]: 
                        k -= 1     
                    j += 1 #increment to not get dupe 
                    k -= 1 #decrement to not get dupe               
            i += 1
            j = i + 1
            k = len(nums) - 1
        return results
