class Solution:

    def maxTurbulenceSize(self, arr: List[int]) -> int:

        max_length = 1
        n = len(arr)

        if n == 1:
            return 1

        from collections import deque
        q = deque()

        # Initial state
        if arr[0] < arr[1]:
            q.append((1, '<', 2))
            max_length = 2

        elif arr[0] > arr[1]:
            q.append((1, '>', 2))
            max_length = 2

        else:
            q.append((1, '=', 1))

        # state = (element_index, sign, length)

        while q:

            element_index, sign, length = q.popleft()

            if element_index + 1 < n:

                # ---------------------------------
                # Previous sign is <
                # ---------------------------------

                if sign == '<' and arr[element_index] > arr[element_index + 1]:

                    # < >
                    # Signs alternate, so extend
                    new_index = element_index + 1
                    new_length = length + 1
                    new_sign = '>'

                    max_length = max(max_length, new_length)

                    q.append((new_index, new_sign, new_length))

                elif sign == '<' and arr[element_index] < arr[element_index + 1]:

                    # < <
                    # Same sign, so start a new sequence
                    new_index = element_index + 1
                    new_length = 2
                    new_sign = '<'

                    max_length = max(max_length, new_length)

                    q.append((new_index, new_sign, new_length))

                elif sign == '<' and arr[element_index] == arr[element_index + 1]:

                    # Equal breaks turbulence
                    new_index = element_index + 1
                    new_length = 1
                    new_sign = '='

                    q.append((new_index, new_sign, new_length))


                # ---------------------------------
                # Previous sign is >
                # ---------------------------------

                elif sign == '>' and arr[element_index] < arr[element_index + 1]:

                    # > <
                    # Signs alternate, so extend
                    new_index = element_index + 1
                    new_length = length + 1
                    new_sign = '<'

                    max_length = max(max_length, new_length)

                    q.append((new_index, new_sign, new_length))

                elif sign == '>' and arr[element_index] > arr[element_index + 1]:

                    # > >
                    # Same sign, so start a new sequence
                    new_index = element_index + 1
                    new_length = 2
                    new_sign = '>'

                    max_length = max(max_length, new_length)

                    q.append((new_index, new_sign, new_length))

                elif sign == '>' and arr[element_index] == arr[element_index + 1]:

                    # Equal breaks turbulence
                    new_index = element_index + 1
                    new_length = 1
                    new_sign = '='

                    q.append((new_index, new_sign, new_length))


                # ---------------------------------
                # Previous sign is =
                # ---------------------------------

                elif sign == '=' and arr[element_index] < arr[element_index + 1]:

                    # Start a new turbulent pair
                    new_index = element_index + 1
                    new_length = 2
                    new_sign = '<'

                    max_length = max(max_length, new_length)

                    q.append((new_index, new_sign, new_length))

                elif sign == '=' and arr[element_index] > arr[element_index + 1]:

                    # Start a new turbulent pair
                    new_index = element_index + 1
                    new_length = 2
                    new_sign = '>'

                    max_length = max(max_length, new_length)

                    q.append((new_index, new_sign, new_length))

                elif sign == '=' and arr[element_index] == arr[element_index + 1]:

                    # Still equal
                    new_index = element_index + 1
                    new_length = 1
                    new_sign = '='

                    q.append((new_index, new_sign, new_length))

        return max_length