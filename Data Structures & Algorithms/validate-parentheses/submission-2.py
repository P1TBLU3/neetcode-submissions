class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(","}":"{","]":"["}

        for char in s:
            if char in mapping:
                if not mapping or len(stack) == 0:
                    return False
                aux = stack.pop()
                if mapping[char] != aux:
                    return False

                
            else:
                stack.append(char)


        return len(stack) == 0