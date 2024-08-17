class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for num in asteroids:
            while stack and stack[-1] > 0 and num < 0:
                if abs(num) > abs(stack[-1]):
                    stack.pop()
                elif abs(num) == abs(stack[-1]):
                    stack.pop()
                    num = 0  
                    break
                else:
                    num = 0
                    break
            if num: 
                stack.append(num)
        return stack