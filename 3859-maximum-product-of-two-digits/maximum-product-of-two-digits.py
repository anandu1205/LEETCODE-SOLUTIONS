class Solution:
    def maxProduct(self, n: int) -> int:
        list1=[]
        while n>0:
            rem=n%10
            list1.append(rem)
            n=n//10
        list1.sort(reverse=True)
        return list1[0]*list1[1]

        