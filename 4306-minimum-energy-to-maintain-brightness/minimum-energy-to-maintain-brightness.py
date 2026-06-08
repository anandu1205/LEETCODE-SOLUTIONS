from typing import List

class Solution:
    def minEnergy(
        self,
        n: int,
        brightness: int,
        intervals: List[List[int]]
    ) -> int:
        intervals.sort()

        total_time = 0
        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:
            # The intervals overlap or contain consecutive integer times.
            if start <= current_end + 1:
                current_end = max(current_end, end)
            else:
                total_time += current_end - current_start + 1
                current_start, current_end = start, end

        # Include the final merged interval.
        total_time += current_end - current_start + 1

        bulbs_needed = (brightness + 2) // 3

        return total_time * bulbs_needed