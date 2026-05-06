class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import deque,defaultdict
        graph=defaultdict(list)
        queue=deque()
        in_degree=[0]*numCourses
        for a,b in prerequisites:
            graph[a].append(b)
            in_degree[b]+=1
        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        prereq=[set()for _ in range (numCourses)]
        while queue:
            node=queue.popleft()
            for nei in graph[node]:
                prereq[nei].add(node)
                prereq[nei].update(prereq[node])
                in_degree[nei]-=1
                if in_degree[nei]==0:
                    queue.append(nei)
        answer=[]
        for u,v in queries:
            answer.append(u in prereq[v])
        return answer



        