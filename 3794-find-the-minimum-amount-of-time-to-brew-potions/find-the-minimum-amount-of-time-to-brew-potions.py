class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + skill[i]

        start = 0

        for j in range(1, m):
            next_start = 0

            for i in range(n):
                prev_finish_on_wizard_i = start + mana[j - 1] * prefix[i + 1]
                new_reach_wizard_i = mana[j] * prefix[i]

                next_start = max(
                    next_start,
                    prev_finish_on_wizard_i - new_reach_wizard_i
                )

            start = next_start

        return start + mana[-1] * prefix[n]