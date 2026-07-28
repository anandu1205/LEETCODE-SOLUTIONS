class Solution:
    def maxTotalValue(self, value: List[int], decay: List[int], m: int) -> int:
        MOD = 10 ** 9 + 7

        def count_and_sum(threshold):
            cnt = 0
            total = 0

            for a, d in zip(value, decay):
                if a < threshold:
                    continue

                k = (a - threshold) // d + 1
                cnt += k
                total += k * (2 * a - (k - 1) * d) // 2

            return cnt, total

        # Total positive terms
        total_cnt, total_sum = count_and_sum(1)

        if total_cnt <= m:
            return total_sum % MOD

        lo, hi = 1, max(value)

        while lo < hi:
            mid = (lo + hi + 1) // 2
            cnt, _ = count_and_sum(mid)

            if cnt >= m:
                lo = mid
            else:
                hi = mid - 1

        L = lo

        cnt_gt, sum_gt = count_and_sum(L + 1)

        ans = sum_gt + (m - cnt_gt) * L

        return ans % MOD
        