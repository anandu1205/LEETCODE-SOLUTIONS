class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=str(n)
        x=""
        sum=0
        for i in range(len(s)):
            if s[i]!="0":
                x+=s[i]
        if x=="":
            x="0"
        for i in range(len(x)):
            sum+=int(x[i])
        return sum*int(x)
        