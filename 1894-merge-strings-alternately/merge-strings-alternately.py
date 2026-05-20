class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        wp1 = 0
        wp2 = 0

        length1 = len(word1)
        length2 = len(word2)

        ans = ""

        min_length = min(length1, length2)

        while wp1 < min_length:

            ans += word1[wp1]
            ans += word2[wp2]

            wp1 += 1
            wp2 += 1

        # add remaining part
        ans += word1[wp1:]
        ans += word2[wp2:]

        return ans