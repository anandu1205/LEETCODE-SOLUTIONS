class Solution:
    def minChanges(self, s: str) -> int:
        length=len(s)
        pointer=0
        list1=[]
        while pointer<length:
            sub_string=s[pointer:pointer+2]
            pointer+=2
            list1.append(sub_string)
        changes=0
        for substring in list1:
            if substring=="10":
                changes+=1
            if substring=="01":
                changes+=1
        return changes