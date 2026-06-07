from typing import List

class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: List[List[int]]) -> int:
        intervals.sort()

        total_time = 0
        start, end = intervals[0]

        for s, e in intervals[1:]:
            if s <= end + 1:
                end = max(end, e)
            else:
                total_time += end - start + 1
                start, end = s, e

        total_time += end - start + 1

        bulbs_needed = (brightness + 2) // 3  # ceil(brightness / 3)

        return total_time * bulbs_needed