class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Store the final index of every character.
        last_occurrence = {}

        for index, char in enumerate(s):
            last_occurrence[char] = index

        result = []
        partition_start = 0
        partition_end = 0

        for index, char in enumerate(s):
            # Extend the partition to include every occurrence
            # of the current character.
            partition_end = max(
                partition_end,
                last_occurrence[char]
            )

            # The current partition is complete when we reach
            # its furthest required index.
            if index == partition_end:
                partition_length = partition_end - partition_start + 1
                result.append(partition_length)

                partition_start = index + 1

        return result
        