class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        result = []
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            # If previous kept interval covers current interval, skip current.
            if result[-1][0] <= intervals[i][0] and intervals[i][1] <= result[-1][1]:
                continue
            else:
                result.append(intervals[i])

        return len(result)