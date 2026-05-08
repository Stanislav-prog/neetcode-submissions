class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = s.replace(" ", "").lower()
        s1 = "".join(filter(str.isalnum, formatted_s))

        reversed_s = formatted_s[::-1]
        s2 = "".join(filter(str.isalnum, reversed_s))
        
        return s1 == s2