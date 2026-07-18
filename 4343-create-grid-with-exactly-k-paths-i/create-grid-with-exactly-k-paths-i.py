class Solution:
    def createGrid(self, m: int, n: int, k: int) -> List[str]:
        grid = [["#"] * n for _ in range(m)]

        def carve_corridor(r, c):
            # go right to last column
            while c < n:
                grid[r][c] = "."
                c += 1

            c = n - 1

            # go down to last row
            while r < m:
                grid[r][c] = "."
                r += 1

        if k == 1:
            carve_corridor(0, 0)

        elif k == 2:
            if m < 2 or n < 2:
                return []

            for r in range(2):
                for c in range(2):
                    grid[r][c] = "."

            carve_corridor(1, 1)

        elif k == 3:
            if m >= 2 and n >= 3:
                for r in range(2):
                    for c in range(3):
                        grid[r][c] = "."

                carve_corridor(1, 2)

            elif m >= 3 and n >= 2:
                for r in range(3):
                    for c in range(2):
                        grid[r][c] = "."

                carve_corridor(2, 1)

            else:
                return []

        elif k == 4:
            if m >= 2 and n >= 4:
                for r in range(2):
                    for c in range(4):
                        grid[r][c] = "."

                carve_corridor(1, 3)

            elif m >= 4 and n >= 2:
                for r in range(4):
                    for c in range(2):
                        grid[r][c] = "."

                carve_corridor(3, 1)

            elif m >= 3 and n >= 3:
                for r in range(3):
                    for c in range(3):
                        grid[r][c] = "."

                # full 3x3 has 6 paths.
                # Block top-right and bottom-left to leave exactly 4.
                grid[0][2] = "#"
                grid[2][0] = "#"

                carve_corridor(2, 2)

            else:
                return []

        return ["".join(row) for row in grid]