class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]

        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        visited = set()
        stack = [1]
        ans = float("inf")

        while stack:
            city = stack.pop()

            if city in visited:
                continue

            visited.add(city)

            for nei, dist in graph[city]:
                ans = min(ans, dist)

                if nei not in visited:
                    stack.append(nei)

        return ans