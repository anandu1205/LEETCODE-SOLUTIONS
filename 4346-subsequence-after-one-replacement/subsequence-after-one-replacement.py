class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        m = len(s)

        for c in t:
            if s[i] == c:
                i += 1

            i = max(i, j + 1)

            if s[j] == c:
                j += 1

            if i == m or j == m:
                return True

        return False