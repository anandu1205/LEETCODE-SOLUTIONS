class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        best_left = 0
        ans = 0

        for j in range(k, len(nums)):
            best_left = max(best_left, nums[j - k])
            ans = max(ans, best_left + nums[j])

        return ans
        