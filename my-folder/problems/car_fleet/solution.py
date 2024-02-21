class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        steps = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, sp in steps:
            time = (target-pos)/sp
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return(len(stack))