class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import deque
        n=len(arr)
        visited=[False]*n
        queue=deque([start])
        while queue:
            i=queue.popleft()
            if arr[i]==0:
                return True
            if visited[i]:
                continue
            visited[i]=True
            if i+arr[i]<n and i+arr[i]>0:
                queue.append(i+arr[i])
            if i-arr[i]<n and i-arr[i]>=0:
                queue.append(i-arr[i])
        return False
            
        