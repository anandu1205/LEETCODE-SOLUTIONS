class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:

        import heapq
        from collections import defaultdict

        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))

        # cost, node, stops
        pq = [(0, src, 0)]

        # dist[node][stops]
        dist = {}

        while pq:

            cost, node, stops = heapq.heappop(pq)

            if node == dst:
                return cost

            if stops > k:
                continue

            if (node, stops) in dist and dist[(node, stops)] < cost:
                continue

            for nei, price in graph[node]:

                new_cost = cost + price

                if (nei, stops + 1) not in dist or new_cost < dist[(nei, stops + 1)]:

                    dist[(nei, stops + 1)] = new_cost

                    heapq.heappush(
                        pq,
                        (new_cost, nei, stops + 1)
                    )

        return -1

        