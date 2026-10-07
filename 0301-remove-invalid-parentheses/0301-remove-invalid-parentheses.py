class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        # Find minimum number of '(' and ')' to remove
        left = right = 0

        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        result = set()

        def backtrack(index, path, open_count, close_count, rem_left, rem_right):
            if index == len(s):
                if rem_left == 0 and rem_right == 0 and open_count == close_count:
                    result.add("".join(path))
                return

            ch = s[index]

            # Remove '('
            if ch == '(' and rem_left > 0:
                backtrack(
                    index + 1, path,
                    open_count, close_count,
                    rem_left - 1, rem_right
                )

            # Remove ')'
            if ch == ')' and rem_right > 0:
                backtrack(
                    index + 1, path,
                    open_count, close_count,
                    rem_left, rem_right - 1
                )

            # Keep current character
            if ch == '(':
                path.append(ch)
                backtrack(
                    index + 1, path,
                    open_count + 1, close_count,
                    rem_left, rem_right
                )
                path.pop()

            elif ch == ')':
                if open_count > close_count:
                    path.append(ch)
                    backtrack(
                        index + 1, path,
                        open_count, close_count + 1,
                        rem_left, rem_right
                    )
                    path.pop()

            else:
                path.append(ch)
                backtrack(
                    index + 1, path,
                    open_count, close_count,
                    rem_left, rem_right
                )
                path.pop()

        backtrack(0, [], 0, 0, left, right)

        return list(result)
        