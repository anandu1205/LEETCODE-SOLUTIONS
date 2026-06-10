from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        even_cost = [0] * k
        odd_cost = [0] * k

        for index, num in enumerate(nums):
            remainder = num % k

            for target in range(k):
                increase = (target - remainder) % k
                decrease = (remainder - target) % k
                cost = min(increase, decrease)

                if index % 2 == 0:
                    even_cost[target] += cost
                else:
                    odd_cost[target] += cost

        answer = float("inf")

        for x in range(k):
            for y in range(k):
                if x != y:
                    answer = min(
                        answer,
                        even_cost[x] + odd_cost[y]
                    )

        return answer
        