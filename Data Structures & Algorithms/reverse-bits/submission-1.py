class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if ((n >> i) & 1): # extract ith bit of n, if 1
                res |= (1 << (31 - i)) #shift ith bit in res to 31-i
        return res
