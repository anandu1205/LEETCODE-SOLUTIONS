class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        arr = []

        for r in range(m):
            for c in range(n):
                arr.append(grid[r][c])

        total = m * n
        k = k % total

        arr = arr[-k:] + arr[:-k]

        res = []

        index = 0
        for r in range(m):
            row = []
            for c in range(n):
                row.append(arr[index])
                index += 1
            res.append(row)

        return res