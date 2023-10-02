class Solution:
    def ispar(self, x):
        stack = []  # Initialize an empty stack to store opening parentheses

        for char in x:
            if char in "({[":
                stack.append(char)  # Push opening parentheses onto the stack
            else:
                # If it's a closing parenthesis, check if the stack is empty
                if not stack:
                    return False  # There's no matching opening parenthesis

                # Pop the top element from the stack and check if it matches the current closing parenthesis
                top = stack.pop()
                if (char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '['):
                    return False  # Mismatched parentheses

        # After processing all characters, if the stack is empty, it's balanced
        return len(stack) == 0

# Example usage:
s = Solution()
x = "({[()]})"
result = s.ispar(x)
if result:
    print("The given string is balanced.")
else:
    print("The given string is not balanced.")
