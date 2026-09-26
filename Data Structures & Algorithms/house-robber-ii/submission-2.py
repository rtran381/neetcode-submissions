class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(i, arr, hashmap):
            if i >= len(arr):
                return 0
            if i in hashmap:
                return hashmap[i]
            hashmap[i] = max(arr[i] + dfs(i + 2, arr, hashmap), dfs(i + 1, arr, hashmap))
            return hashmap[i]
        return max(dfs(0, nums[1:], {}), dfs(0, nums[:len(nums) - 1], {}))