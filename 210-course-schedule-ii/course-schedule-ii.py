from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        queue = deque()
        result = []
        in_degree = [0] * numCourses

        # FIX 1: correct variable name
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # initial zero indegree nodes
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbour in graph[node]:
                # FIX 2: update neighbour
                in_degree[neighbour] -= 1

                # FIX 3: check neighbour
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        return result if len(result) == numCourses else []
        