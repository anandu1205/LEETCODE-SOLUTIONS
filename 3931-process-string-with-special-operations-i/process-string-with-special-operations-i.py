class Solution:
    def processStr(self, s: str) -> str:
        result=""
        for i in range(len(s)):
            if s[i] in "abcdefghjknopqrstuvwxyzilm":
                result+=s[i]
            elif s[i]=='*':
                result=result[:-1]
            elif s[i]=='#':
                result+=result
            elif s[i]=='%':
                result=result[::-1]
        return result
        