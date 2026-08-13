class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = dict()

        for word in strs:
            alp = [0] * 26
            for letter in word:
                alp[ord(letter) - ord('a')] += 1
            
            if(tuple(alp) in d1):
                d1[tuple(alp)].append(word)
            else:
                d1[tuple(alp)] = list()
                d1[tuple(alp)].append(word)
        
        return list(d1.values())



        