class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        # We can modify 'n' directly instead of using 'count'
        while True:
            prod = 1
            temp = n
            
            # Extract digits mathematically (faster than string conversion)
            while temp > 0:
                prod *= temp % 10
                temp //= 10
                
            # If the product is divisible by t, we found our answer
            if prod % t == 0:
                return n
            
            # Otherwise, check the next number
            n += 1