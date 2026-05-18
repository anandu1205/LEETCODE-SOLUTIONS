class Solution:
    def isValid(self, s: str) -> bool:
        dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for ch in s:

            # opening brackets
            if ch in "({[":
                stack.append(ch)

            # closing brackets
            else:
                if not stack:
                    return False

                top = stack.pop()

                if dict[top] != ch:
                    return False

        return len(stack) == 0