class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        hashmap = {}
        def dfs(val):
            if val == 0:
                return 0
            if val in hashmap:
                return hashmap[val]
            hashmap[val] = float("inf")
            for c in coins:
                if c <= val:
                    hashmap[val] = min(hashmap[val], 1 + dfs(val - c))
            return hashmap[val]
        minimum = dfs(amount)

        return -1 if minimum >= float("inf") else minimum