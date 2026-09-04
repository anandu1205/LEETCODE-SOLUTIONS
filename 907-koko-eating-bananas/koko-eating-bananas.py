class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        
        l, r = 1, max(piles)
        ans = r
        
        while l <= r:
            m = (l + r) // 2
            
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            
            if hours <= h:
                ans = m        # valid answer
                r = m - 1      # try smaller speed
            else:
                l = m + 1      # need faster speed
        
        return ans
        