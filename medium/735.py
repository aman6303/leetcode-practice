from collections import deque


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def is_sign_same(a, b):
            if a > 0 and b > 0:
                return True
            elif a < 0 and b < 0:
                return True
            else:
                return False

        stack = deque()
        stack.append(asteroids[0])
        for ast in asteroids[1:]:
            # breakpoint()
            if is_sign_same(ast, stack[-1]):
                stack.append(ast)
            else:
                if abs(ast) > abs(stack[-1]):
                    stack.pop()
                    stack.append(ast)

                elif abs(ast) == abs(stack[-1]):
                    stack.pop()
                    # breakpoint()
                else:
                    continue
        breakpoint()
        return list(stack)


Solution().asteroidCollision(asteroids=[5, 10, -5])
