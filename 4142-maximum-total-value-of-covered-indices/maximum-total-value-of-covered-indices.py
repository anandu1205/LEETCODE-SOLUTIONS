from typing import List

class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)
        l = 0
        answer = 0

        while l < n:
            # Search for the beginning of the next group of ones.
            if s[l] != '1':
                l += 1
                continue

            # Find the first position after this group of ones.
            r = l

            while r < n and s[r] == '1':
                r += 1

            # The group occupies indices [l, r - 1].
            if l == 0:
                answer += sum(nums[l:r])
            else:
                possible_values = nums[l - 1:r]
                answer += sum(possible_values) - min(possible_values)

            l = r

        return answer