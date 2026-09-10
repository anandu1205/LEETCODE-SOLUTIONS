class Solution:
    def countSpecialIntegers(self, nums: List[int]) -> int:
        first = {}
        last = {}
        freq = {}

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i

            last[x] = i
            freq[x] = freq.get(x, 0) + 1

        ans = 0

        for x in freq:
            if last[x] - first[x] + 1 == freq[x]:
                ans += 1

        return ans