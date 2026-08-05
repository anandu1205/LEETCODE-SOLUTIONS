from typing import List
from collections import defaultdict, deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in invocations:
            graph[a].append(b)

        suspicious = set()
        queue = deque([k])

        while queue:
            node = queue.popleft()

            if node in suspicious:
                continue

            suspicious.add(node)

            for nei in graph[node]:
                queue.append(nei)

        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        ans = []
        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans