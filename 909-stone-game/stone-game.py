class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        Alice=0
        Bob=0
        n=len(piles)
        while not(n<=0):
            maximum=max(piles[0],piles[-1])
            minimum=min(piles[0],piles[-1])
            Alice+=maximum
            Bob+=minimum
            piles.remove(maximum)
            piles.remove(minimum)
            n-=2
        return Alice>Bob
        