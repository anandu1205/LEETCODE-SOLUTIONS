from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for r in range(9):
            seen = set()

            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in seen:
                    return False

                seen.add(val)

        # Check columns
        for c in range(9):
            seen = set()

            for r in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if val in seen:
                    return False

                seen.add(val)

        # Check 3x3 boxes
        for box_r in range(0, 9, 3):
            for box_c in range(0, 9, 3):
                seen = set()

                for r in range(box_r, box_r + 3):
                    for c in range(box_c, box_c + 3):
                        val = board[r][c]

                        if val == ".":
                            continue

                        if val in seen:
                            return False

                        seen.add(val)

        return True