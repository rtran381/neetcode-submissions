class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def cSum(index, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(index,len(nums)):
                if total + nums[index] <= target:
                    cur.append(nums[j])
                    cSum(j, cur, total + nums[j])
                    cur.pop()
        cSum(0, [], 0)
        return res
            
        
