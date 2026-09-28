class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        ans=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            if s[i]==')':
                stack.pop()
            ans=max(ans,len(stack))
        return ans
        