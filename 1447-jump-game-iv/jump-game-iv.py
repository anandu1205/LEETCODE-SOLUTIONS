class Solution:
    def minJumps(self, arr: List[int]) -> int:

        from collections import defaultdict, deque

        n = len(arr)

        if n == 1:
            return 0

        mp = defaultdict(list)

        for i, val in enumerate(arr):
            mp[val].append(i)

        q = deque([0])

        visited = [False] * n
        visited[0] = True

        steps = 0

        while q:

            size = len(q)

            for _ in range(size):

                node = q.popleft()

                if node == n - 1:
                    return steps

                neighbors = []

                # same value
                neighbors += mp[arr[node]]

                # adjacent
                if node + 1 < n:
                    neighbors.append(node + 1)

                if node - 1 >= 0:
                    neighbors.append(node - 1)

                for nei in neighbors:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)

                mp[arr[node]].clear()

            steps += 1
        