class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Time O(len(stones) * sum(stones)), Memory O(sum(stones))
        dp = {0}
        for weight in stones:
            new_dp = set()
            for s in dp:
                new_dp.add(s+weight)
                new_dp.add(s-weight)
            dp = new_dp
        return min([s if s>=0 else float("inf") for s in dp])