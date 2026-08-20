class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        letters, window = dict(), dict()
        for c in t:
            letters[c] = 1 + letters.get(c, 0)
        need, have = len(letters), 0

        res = s + "1"
        l, r = 0, 0

        while r < len(s): 
            letter = s[r]
            if letter in letters: #add letter if needed for substring
                window[letter] = 1 + window.get(letter, 0)
                if window[letter] == letters[letter]: #increment if category is filled
                    have += 1
            while have == need: #while window has all needed characters
                sub = s[l:r+1]
                if len(sub) < len(res): #update if shorter substring
                    res = sub
                rm = s[l]
                if rm in window: #remove leftmost character
                    window[rm] -= 1
                    if window[rm] < letters[rm]: #check if window no longer meets char req
                        have -= 1
                l += 1
            r += 1
        if res == s + "1": #if res never updated that means no substring availible
            return ""
        else:
            return res
        

