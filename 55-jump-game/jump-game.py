from collections import deque
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        queue = deque([0])   # store indices only
        visited = set([0])

        farthest_processed = 0

        while queue:

            node = queue.popleft()

            if node == n - 1:
                return True

            max_jump = node + nums[node]

            # Only process NEW range
            start = max(farthest_processed + 1, node + 1)

            for next_node in range(start, min(max_jump + 1, n)):

                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(next_node)

            farthest_processed = max(farthest_processed, max_jump)

        return False