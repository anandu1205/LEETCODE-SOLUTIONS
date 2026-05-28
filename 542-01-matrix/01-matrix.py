class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        queue=deque()
        visited=set()
        ans=[[0]*n for _ in range(m)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    queue.append((i,j))
                    visited.add((i,j))
        while queue:
            r,c=queue.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if nr>=0 and nc>=0 and nr<m and nc<n and ((nr,nc)) not in visited:
                    ans[nr][nc]=ans[r][c]+1
                    visited.add((nr,nc))
                    queue.append((nr,nc))
        return ans

       

        