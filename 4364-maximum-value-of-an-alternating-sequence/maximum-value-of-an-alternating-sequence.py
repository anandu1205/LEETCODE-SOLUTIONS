class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        odd_peaks=n//2
        if odd_peaks==0:
            ans1=s
        else:
            ans1=s+odd_peaks*m-(odd_peaks-1)
        even_peaks=(n-1)//2
        ans2=s+even_peaks*(m-1)
        return max(ans1,ans2)
        