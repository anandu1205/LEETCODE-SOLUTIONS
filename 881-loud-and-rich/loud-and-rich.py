class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        from collections import defaultdict,deque
        graph=defaultdict(list)
        n=len(quiet)
        in_degree=[0]*n
        for a,b in richer:
            graph[a].append(b)
            in_degree[b]+=1
        queue=deque()
        answer=list(range(n))  # inital answer is itself
        for i in range(n):
            if in_degree[i]==0:
                queue.append(i)
        while queue:
            node=queue.popleft()
            for nei in graph[node]:
                if quiet[answer[node]]<quiet[answer[nei]]:
                    answer[nei]=answer[node]
                in_degree[nei]-=1
                if in_degree[nei]==0:
                    queue.append(nei)
        return answer


        