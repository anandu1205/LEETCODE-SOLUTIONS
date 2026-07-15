class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict,deque
        graph=defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited=set()
        queue=deque()
        ans=0
        for i in range(n):
            if i in visited:
                continue
            queue.append(i)
            component=[]
            while queue:
                node=queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                component.append(node)
                for nei in graph[node]:
                    if nei not in visited:
                     
                     queue.append(nei)
            k=len(component)
            condition=True
            for node in component:
                if len(graph[node])!=k-1:
                    condition=False
                    break
            if condition:
                ans+=1
        return ans