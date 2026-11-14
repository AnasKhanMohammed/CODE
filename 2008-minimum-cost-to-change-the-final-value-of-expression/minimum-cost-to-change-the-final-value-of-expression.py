class Solution:
    def minOperationsToFlip(self, expression: str) -> int:

        def combine(left, right, op):
            actual = (left[0] & right[0]) if op == '&' else (left[0] | right[0])

            best = [float('inf'), float('inf')]

            for a in (0, 1):
                for b in (0, 1):

                    cost = left[a + 1] + right[b + 1]

                    for flip in (0, 1):
                        new_op = op

                        if flip:
                            new_op = '|' if op == '&' else '&'

                        if new_op == '&':
                            result = a & b
                        else:
                            result = a | b

                        best[result] = min(
                            best[result],
                            cost + flip
                        )

            return (actual, best[0], best[1])

        values = []
        ops = []

        for ch in expression:

            if ch == '0':
                values.append((0, 0, 1))

            elif ch == '1':
                values.append((1, 1, 0))

            elif ch == '(':
                ops.append(ch)

            elif ch == ')':
                while ops and ops[-1] != '(':
                    right = values.pop()
                    left = values.pop()
                    op = ops.pop()

                    values.append(combine(left, right, op))

                ops.pop()

            else:
                while ops and ops[-1] != '(':
                    right = values.pop()
                    left = values.pop()
                    op = ops.pop()

                    values.append(combine(left, right, op))

                ops.append(ch)

        while ops:
            right = values.pop()
            left = values.pop()
            op = ops.pop()

            values.append(combine(left, right, op))

        result = values[0]

        return result[2] if result[0] == 0 else result[1]