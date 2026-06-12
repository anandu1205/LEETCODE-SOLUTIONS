class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            # Odd-length palindromes: center is s[i]
            left = i
            right = i

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                result += 1
                left -= 1
                right += 1

            # Even-length palindromes: center is between i and i + 1
            left = i
            right = i + 1

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                result += 1
                left -= 1
                right += 1

        return result

        