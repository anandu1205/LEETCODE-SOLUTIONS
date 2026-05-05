from collections import defaultdict, deque
from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        
        graph = defaultdict(list)
        indegree = [0] * n
        
        # Step 1: build graph (a -> b)
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        
        # Step 2: initial answer (each person itself)
        answer = list(range(n))
        
        # Step 3: start with richest (indegree = 0)
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        # Step 4: BFS (topological order)
        while q:
            node = q.popleft()
            
            for nei in graph[node]:
                # propagate quieter person
                if quiet[answer[node]] < quiet[answer[nei]]:
                    answer[nei] = answer[node]
                
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return answer