class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(0, n+1):
            res[i] = res[i >> 1] + (i & 1) #previous power of 2 + 1 or 0 depending on the i
        return res
