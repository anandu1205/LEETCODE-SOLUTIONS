class Solution:
    def insert(self, intervals, newInterval):
        res = []

        for i in range(len(intervals)):
            # New interval belongs before everything remaining
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res

            # Current interval belongs before newInterval
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # They overlap
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        res.append(newInterval)
        return res
        