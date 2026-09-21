class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        from collections import Counter
        freq=Counter(nums)
        values=sorted(freq)
        n=len(values)
        dp=[0]*n 
        dp[0]=values[0]*freq[values[0]]
        for i in range(1,n):
            if values[i]==values[i-1]+1:
                if i-2>=0:
                    dp[i]=max(values[i]*freq[values[i]]+dp[i-2],dp[i-1])
                else:
                    dp[i]=max(values[i]*freq[values[i]],dp[i-1])
            else:
                dp[i]=dp[i-1]+values[i]*freq[values[i]]
        return dp[-1]