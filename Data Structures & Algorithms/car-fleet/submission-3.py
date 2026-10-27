class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        position,speed = map(list,zip(*sorted(zip(position,speed))))

        stack = []
        for i in range(len(position) - 1, -1, -1):
            time = (target - position[i] ) / speed[i]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)