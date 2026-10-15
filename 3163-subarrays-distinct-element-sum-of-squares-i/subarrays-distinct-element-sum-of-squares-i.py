
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(n):
            visited = set()

            for j in range(i, n):
                visited.add(nums[j])
                distinct = len(visited)
                total += distinct * distinct

        return total


        