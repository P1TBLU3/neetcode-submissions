class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []
        result = 0

        for token in tokens:
            if token not in "+-*/":
                stack.append( int(token) )
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()

                if token == '+':
                    stack.append(operand_1 + operand_2)
                elif token == '-':
                    stack.append(operand_1 - operand_2)
                elif token == '*':
                    stack.append(operand_1 * operand_2)
                elif token == '/':
                    stack.append(int(operand_1 / operand_2))



        return stack[0]