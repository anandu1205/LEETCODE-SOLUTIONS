class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        unique_nums = sorted(set(nums))

        left = 0
        maximum_kept = 0

        for right in range(len(unique_nums)):
            while unique_nums[right] - unique_nums[left] >= n:
                left += 1

            current_kept = right - left + 1
            maximum_kept = max(maximum_kept, current_kept)

        return n - maximum_kept