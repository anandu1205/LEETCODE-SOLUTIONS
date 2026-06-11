class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        read = 0
        write = 0
        group_start = 0

        while read <= len(chars):
            if (
                read < len(chars)
                and chars[read] == chars[group_start]
            ):
                read += 1
                continue

            size_of_the_group = read - group_start

            chars[write] = chars[group_start]
            write += 1

            if size_of_the_group > 1:
                for digit in str(size_of_the_group):
                    chars[write] = digit
                    write += 1

            if read == len(chars):
                break

            group_start = read

        return write