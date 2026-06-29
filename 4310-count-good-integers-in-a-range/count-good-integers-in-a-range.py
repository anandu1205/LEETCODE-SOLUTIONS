from functools import lru_cache

class Solution:
    def goodIntegers(self, l: int, r: int, k: int) -> int:

        def count(bound: int) -> int:
            if bound < 0:
                return 0

            s = str(bound)
            n = len(s)

            @lru_cache(None)
            def dp(pos: int, prev: int, tight: bool, started: bool) -> int:
                # Built one valid number
                if pos == n:
                    return 1

                limit = int(s[pos]) if tight else 9
                ans = 0

                for digit in range(limit + 1):
                    new_tight = tight and (digit == limit)

                    # Still in leading zeros
                    if not started and digit == 0:
                        ans += dp(pos + 1, 10, new_tight, False)

                    # First non-leading-zero digit
                    elif not started:
                        ans += dp(pos + 1, digit, new_tight, True)

                    # Normal transition
                    elif abs(prev - digit) <= k:
                        ans += dp(pos + 1, digit, new_tight, True)

                return ans

            return dp(0, 10, True, False)

        return count(r) - count(l - 1)