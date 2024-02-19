class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda x,y: x+y, 
            "-": lambda x,y: y-x, 
            "*": lambda x,y: x*y, 
            "/": lambda x,y: y/x
            }
        valid = "-+/*"
        queue = []
        for i, n in enumerate(tokens):
            if n in valid:
                queue.append(operators[n](int(queue.pop()), int(queue.pop())))
            else:
                queue.append(n)
        return int(queue[0])