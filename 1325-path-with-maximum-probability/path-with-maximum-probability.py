class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int
    ) -> float:

        import heapq
        from collections import defaultdict

        graph = defaultdict(list)

        # build graph correctly
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]

            graph[a].append((prob, b))
            graph[b].append((prob, a))

        # max heap using negative probabilities
        pq = [(-1.0, start_node)]

        visited = set()

        while pq:
            curr_prob, node = heapq.heappop(pq)

            curr_prob = -curr_prob

            if node == end_node:
                return curr_prob

            if node in visited:
                continue

            visited.add(node)

            for prob, nei in graph[node]:
                if nei not in visited:
                    new_prob = curr_prob * prob
                    heapq.heappush(pq, (-new_prob, nei))

        return 0.0
        