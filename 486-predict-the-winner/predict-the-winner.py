class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                  dp[i][j]=nums[j]
        for length in range(2,len(nums)+1):
            for i in range(n+1-length):
                j=length-1+i
                takeleft=nums[i]-dp[i+1][j]
                takeright=nums[j]-dp[i][j-1]
                dp[i][j]=max(takeleft,takeright)
        if dp[0][n-1]>=0:
            return True
        else:
            return False
        