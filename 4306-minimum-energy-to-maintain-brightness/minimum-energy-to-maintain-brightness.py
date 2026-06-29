from math import ceil

class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort()

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])

        length = 0

        for start, end in merged:
            length += end - start + 1

        answer = length * ceil(brightness / 3)

        return answer