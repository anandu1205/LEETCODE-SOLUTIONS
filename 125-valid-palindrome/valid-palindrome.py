class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1 = ""

        for ch in s:
            if ch.isalnum():
                s1 += ch.lower()

        l = 0
        r = len(s1) - 1

        while l < r:
            if s1[l] == s1[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
        