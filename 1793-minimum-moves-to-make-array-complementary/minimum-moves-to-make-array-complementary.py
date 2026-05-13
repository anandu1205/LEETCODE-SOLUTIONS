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

            # Assume 2 moves for all sums
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # Improve to 1 move for range [low, high]
            diff[low] -= 1
            diff[high + 1] += 1

            # Improve to 0 moves for exact sum
            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1

        # Find minimum moves using prefix sum
        ans = float('inf')
        current = 0

        for s in range(2, 2 * limit + 1):
            current += diff[s]
            ans = min(ans, current)

        return ans
        

                    

        