from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # Nodes are 1-indexed
        dist = [float('inf')] * (n + 1)

        dist[k] = 0

        pq = [(0, k)]

        while pq:

            curr_time, node = heapq.heappop(pq)

            # Skip stale entries
            if curr_time > dist[node]:
                continue

            for nei, weight in graph[node]:

                new_time = curr_time + weight

                # Relaxation
                if new_time < dist[nei]:

                    dist[nei] = new_time

                    heapq.heappush(pq, (new_time, nei))

        ans = max(dist[1:])

        return ans if ans != float('inf') else -1

        