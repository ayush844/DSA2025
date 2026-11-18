class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)