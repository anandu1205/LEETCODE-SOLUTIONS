class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0 #pointer for s
        j=0 #pointer for t
        length=min(len(s),len(t))
        if len(t)<len(s):
            return False
        while i<length and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i==length

        