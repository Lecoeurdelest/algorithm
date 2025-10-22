class Solution:
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            top = stack[-1] if stack else None
            if top is None and self.pairs.get(char):
                stack.append(char)
            elif self.pairs.get(char) == top and self.pairs.get(char) is not None:
                stack.pop()
            else:
                stack.append(char)
        return True if len(stack) == 0 else False