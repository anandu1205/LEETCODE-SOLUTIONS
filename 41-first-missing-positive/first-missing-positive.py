class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        INF = float("inf")
        mini = INF
        maxi = 0

        for num in nums:
            if num > 0:
                mini = min(mini, num)
                maxi = max(maxi, num)

        # No positive numbers exist.
        if mini == INF:
            return 1

        # If 1 is absent, it is always the answer.
        if mini != 1:
            return 1

        numbers = set(nums)

        for number in range(1, maxi + 1):
            if number not in numbers:
                return number

        return maxi + 1
        