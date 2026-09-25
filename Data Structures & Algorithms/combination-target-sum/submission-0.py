class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def cSum(index, cur, total) -> List[int]:
            if total == target:
                res.append(cur.copy())
                return
            if index >= len(nums) or total > target:
                return
            sub = nums[index:]

            cur.append(nums[index])
            cSum(index, cur, total + nums[index])
            cur.pop()
            
            cSum(index + 1, cur, total)
        cSum(0, [], 0)
        return res
            
        
