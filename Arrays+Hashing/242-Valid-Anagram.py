class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # establish dictionaries for each string
        sDict, tDict = {}, {}
        
        # check length
        if len(s) != len(t):
            return False
        
        # now letters into dictionary - estbalish them as 0 and then add one for each including the first
        for l in range(len(s)):
            sDict[s[l]] = sDict.get(s[l],0)+1
            tDict[t[l]] = tDict.get(t[l],0)+1
        # for every pair in the sDict pull the corresponding letter's pair in tDict and check that they are the same
        # if not False
        for pair in sDict:
            if sDict[pair] != tDict.get(pair):
                return False
        return True # anagrams
