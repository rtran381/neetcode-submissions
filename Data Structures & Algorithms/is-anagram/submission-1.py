class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = dict()
        d2 = dict()

        for letter in s:
            d1[letter] = d1.get(letter, 0) + 1

        for letter in t:
            d2[letter] = d2.get(letter, 0) + 1

        if d1 == d2:
            return True
        return False