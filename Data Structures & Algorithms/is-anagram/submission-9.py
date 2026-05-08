class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenS, seenT = {}, {}

        for i in range(len(s)):
            seenS[s[i]] = seenS.get(s[i], 0) + 1
            seenT[t[i]] = seenT.get(t[i], 0) + 1

        print(seenS.keys(), seenT.keys())

        for key in seenS.keys():
            if seenS.get(key) != seenT.get(key, 0):
                return False
        return True 