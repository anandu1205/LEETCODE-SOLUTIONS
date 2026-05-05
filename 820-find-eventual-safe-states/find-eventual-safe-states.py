class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        
        n = len(graph)
        out_degree = [0] * n
        
        # Step 1: compute out_degree
        for i in range(n):
            out_degree[i] = len(graph[i])
        
        # Step 2: reverse graph
        reverse_graph = defaultdict(list)
        for i in range(n):
            for j in graph[i]:
                reverse_graph[j].append(i)
        
        # Step 3: queue with terminal nodes
        queue = deque()
        for i in range(n):
            if out_degree[i] == 0:
                queue.append(i)
        
        safe = [False] * n
        
        # Step 4: BFS
        while queue:
            node = queue.popleft()
            safe[node] = True
            
            for prev in reverse_graph[node]:
                out_degree[prev] -= 1
                if out_degree[prev] == 0:
                    queue.append(prev)
        
        # Step 5: collect result
        result = []
        for i in range(n):
            if safe[i]:
                result.append(i)
        
        return sorted(result)
        
        