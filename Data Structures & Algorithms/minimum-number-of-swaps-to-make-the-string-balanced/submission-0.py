class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = []

        for c in s:
            if c == '[':
                swaps.append(c)
            elif len(swaps) > 0:
                swaps.pop()
        
        return (len(swaps) + 1) // 2
        