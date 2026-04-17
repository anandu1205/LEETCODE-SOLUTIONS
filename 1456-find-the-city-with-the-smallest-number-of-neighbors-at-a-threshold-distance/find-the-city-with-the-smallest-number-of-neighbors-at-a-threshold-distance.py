from typing import List
import heapq
from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(start):
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            
            while heap:
                distance, node = heapq.heappop(heap)
                
                if distance > dist[node]:
                    continue
                
                for nei, weight in graph[node]:
                    new_dist = distance + weight
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(heap, (new_dist, nei))
            
            # count reachable cities
            count = 0
            for i in range(n):
                if i != start and dist[i] <= distanceThreshold:
                    count += 1
            
            return count
        
        min_count = float('inf')
        result = -1
        
        for city in range(n):
            count = dijkstra(city)
            
            # tie-breaking: pick larger index if equal
            if count <= min_count:
                min_count = count
                result = city
        
        return result
        