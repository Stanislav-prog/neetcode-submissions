class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sSorted = "".join(sorted(s))
        tSorted = "".join(sorted(t))

        for i in range(len(sSorted)):
            if sSorted[i] != tSorted[i]:
                return False
        return True