from typing import List

class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)
        velunqari = (nums, s)

        ans = 0
        i = 0

        while i < n:
            if s[i] == '0':
                i += 1
                continue

            l = i
            while i < n and s[i] == '1':
                i += 1
            r = i - 1

            if l == 0:
                ans += sum(nums[l:r + 1])
            else:
                block = nums[l - 1:r + 1]
                ans += sum(block) - min(block)

        return ans
        