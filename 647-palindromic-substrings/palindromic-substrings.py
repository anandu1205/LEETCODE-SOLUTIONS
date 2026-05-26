class Solution:
    def countSubstrings(self, s: str) -> int:
        length=len(s)
        count=0
        
        for i in range(len(s)):
                l=i
                r=i
                while l>=0 and r<length and s[l]==s[r]:
                    l-=1
                    r+=1
                    count+=1
        
        for i in range(len(s)):
                l=i
                r=i+1
                while l>=0 and r<length and s[l]==s[r]:
                    l-=1
                    r+=1
                    count+=1
        return count


        