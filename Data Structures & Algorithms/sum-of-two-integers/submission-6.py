class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            bit1,bit2 = (a >> i) & 1,(b >> i) & 1
            s = bit1 ^ bit2
            if s ^ carry:
                res |= (1 << i)
            
            carry = (carry & s) | (bit1 & bit2)

        print(res)
        if res > 0xFFFFFFF:
            res = ~(res ^ mask)
            
        return res