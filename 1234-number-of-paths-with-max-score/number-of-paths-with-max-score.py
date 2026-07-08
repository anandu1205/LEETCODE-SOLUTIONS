class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        directions = [(-1, 0), (0, -1), (-1, -1)]

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == "X" or ways[r][c] == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != "X":
                        add = 0 if board[nr][nc] == "E" else int(board[nr][nc])
                        new_score = score[r][c] + add

                        if new_score > score[nr][nc]:
                            score[nr][nc] = new_score
                            ways[nr][nc] = ways[r][c]
                        elif new_score == score[nr][nc]:
                            ways[nr][nc] = (ways[nr][nc] + ways[r][c]) % MOD

        if ways[0][0] == 0:
            return [0, 0]

        return [score[0][0], ways[0][0]]