class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total=0
        for i in range(num1,num2+1):
            s=str(i)
            length=len(s)
            if length<3:
                total=total+0
            for i in range(length):
                if 0<=i-1<len(s) and 0<=i+1<len(s):
                    if int(s[i])>int(s[i-1]) and int(s[i])>int(s[i+1]):
                        total+=1
                    elif int(s[i])<int(s[i-1]) and int(s[i])<int(s[i+1]):
                        total+=1
        return total
        