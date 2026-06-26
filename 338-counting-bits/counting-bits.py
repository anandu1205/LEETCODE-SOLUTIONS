class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        for i in range(0,n+1):
            s=str(format(i, "b"))
            count=0
            for char in s:
                if char=="1":
                    count+=1
            dp[i]=count
        return dp
        