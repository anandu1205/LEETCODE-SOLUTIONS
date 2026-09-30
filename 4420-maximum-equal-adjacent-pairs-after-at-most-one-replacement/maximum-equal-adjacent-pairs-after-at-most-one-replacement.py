class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        from collections import defaultdict

        n = len(nums)

        if n < 2:
            return 0

        adj_counter = defaultdict(int)
        init = 0

        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                init += 1

        for i in range(n):
            if i > 0 and nums[i - 1] != nums[i]:
                adj_counter[(nums[i], nums[i - 1])] += 1

            if i + 1 < n and nums[i + 1] != nums[i]:
                adj_counter[(nums[i], nums[i + 1])] += 1

        if not adj_counter:
            return init

        return init + max(adj_counter.values())