class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        operations=[1,5,15,60]
        count=0
        curr=int(current[:2])*60 + int(current[3:])
        corr=int(correct[:2])*60 + int(correct[3:])
        diffrence=corr-curr
        INF=float('inf')
        dp=[INF]*(diffrence+1)
        dp[0]=0
        for i in range(1,diffrence+1):
            for operation in operations:
                if i-operation>=0:
                    dp[i]=min(dp[i],1+dp[i-operation])
        return dp[diffrence]
        
        