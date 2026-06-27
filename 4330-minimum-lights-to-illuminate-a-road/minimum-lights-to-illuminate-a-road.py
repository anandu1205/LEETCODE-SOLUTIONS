class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)

        # Difference array for existing bulbs
        diff = [0] * (n + 1)

        for i, v in enumerate(lights):
            if v == 0:
                continue

            left = max(0, i - v)
            right = min(n - 1, i + v)

            diff[left] += 1
            if right + 1 < n:
                diff[right + 1] -= 1

        # Build illuminated array
        illuminated = [False] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            illuminated[i] = cur > 0

        ans = 0
        i = 0

        while i < n:
            if illuminated[i]:
                i += 1
                continue

            # Place new bulb as far right as possible
            bulb = min(i + 1, n - 1)

            for j in range(max(0, bulb - 1), min(n - 1, bulb + 1) + 1):
                illuminated[j] = True

            ans += 1

        return ans