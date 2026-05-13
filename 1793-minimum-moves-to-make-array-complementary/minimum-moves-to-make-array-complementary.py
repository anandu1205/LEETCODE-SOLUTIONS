class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        n = len(nums)

        # Difference array
        diff = [0] * (2 * limit + 2)

        # Process each pair
        for i in range(n // 2):

            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            pair_sum = a + b

            # Initially assume every sum needs 2 moves
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # Sums achievable in 1 move
            diff[low] -= 1
            diff[high + 1] += 1

            # Exact current sum needs 0 moves
            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1

        # Prefix sum to compute moves for each target sum
        ans = float('inf')
        current = 0

        for target_sum in range(2, 2 * limit + 1):
            current += diff[target_sum]
            ans = min(ans, current)

        return ans
        