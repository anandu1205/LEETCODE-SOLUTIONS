class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        initial_odd=1
        initial_even=0
        odd_sum=1
        sum_even=0
        i=2
        while i<=n:
            initial_odd+=2
            initial_even+=2
            odd_sum+=initial_odd
            sum_even+=initial_even
            i+=1

        minimum=min(odd_sum,sum_even)
        maximum=max(odd_sum,sum_even)
        while minimum:
            maximum,minimum=minimum,maximum%minimum
        return maximum

        