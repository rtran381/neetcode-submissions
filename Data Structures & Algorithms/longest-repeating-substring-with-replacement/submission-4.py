class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        letters = dict()

        res = 0
        l, r = 0, 0


        while r < len(s):
            letter = s[r]
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
            rep = (r - l + 1) - max(letters.values())
            if rep > k:
                letters[s[l]] -= 1
                l += 1
            else:
                res = max(res, r - l + 1)
            r += 1
                

        return res

