class Solution:
    def jump(self, nums: List[int]) -> int:

        import heapq

        last = len(nums) - 1

        visited = set([0])

        pq = [(0, 0)]   # (jumps_taken, node)

        while pq:

            no_of_steps, node = heapq.heappop(pq)

            if node == last:
                return no_of_steps

            for i in range(1, nums[node] + 1):

                next_node = node + i

                if next_node < len(nums) and next_node not in visited:

                    visited.add(next_node)

                    heapq.heappush(
                        pq,
                        (no_of_steps + 1, next_node)
                    )


        