from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        counts = sorted(freq.values(), reverse=True)

        total = 0

        for i, count in enumerate(counts):
            presses = (i // 8) + 1
            total += count * presses

        return total
        