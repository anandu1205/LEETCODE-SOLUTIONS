class Solution:
    def minJumps(self, arr: List[int]) -> int:

        from collections import defaultdict
        import heapq

        n = len(arr)

        # value -> indices
        mp = defaultdict(list)

        for i, val in enumerate(arr):
            mp[val].append(i)

        visited = [False] * n

        pq = [(0, 0)]   # (steps, index)

        while pq:

            steps, node = heapq.heappop(pq)

            if node == n - 1:
                return steps

            if visited[node]:
                continue

            visited[node] = True

           
            if node + 1 < n and not visited[node + 1]:
                heapq.heappush(pq, (steps + 1, node + 1))

            
            if node - 1 >= 0 and not visited[node - 1]:
                heapq.heappush(pq, (steps + 1, node - 1))

            
            for nei in mp[arr[node]]:
                if not visited[nei]:
                    heapq.heappush(pq, (steps + 1, nei))

           
            mp[arr[node]].clear()
        