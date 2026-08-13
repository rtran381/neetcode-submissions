class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        res = 0
        l, r = 0, 0
        letter = set()
        
        while r < len(s):
            c = s[r]
            
            if c not in letter:
                letter.add(c)
                r += 1
            else:
                letter.remove(s[l])
                l += 1
            res = max(res, r - l)
        return res
            