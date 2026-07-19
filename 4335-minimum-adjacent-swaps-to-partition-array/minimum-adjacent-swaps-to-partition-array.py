class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7

        middle_count = 0
        large_count = 0
        swaps = 0

        for x in nums:
            if x < a:
                swaps += middle_count + large_count
            elif x <= b:
                swaps += large_count
                middle_count += 1
            else:
                large_count += 1

        return swaps % MOD