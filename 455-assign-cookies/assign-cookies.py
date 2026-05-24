class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        greedy_pointer=0
        cookie_pointer=0
        g.sort()
        s.sort()
        while  greedy_pointer<len(g) and cookie_pointer<len(s):
            if s[cookie_pointer]>=g[greedy_pointer]:
                greedy_pointer+=1
                cookie_pointer+=1
            else:
                cookie_pointer+=1
        return greedy_pointer
        