class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        stack = []
        nums = 0
        op = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                nums = nums * 10 + int(char)
            if (not char.isdigit()) or i == len(s) - 1:
                if op == '+':
                    stack.append(nums)
                elif op == '-':
                    stack.append(- nums)
                elif op == '*':
                    stack.append(stack.pop() * nums)
                else:
                    prev = stack.pop()
                    stack.append(int(prev / nums))
                op = char
                nums = 0

        return sum(stack)
        