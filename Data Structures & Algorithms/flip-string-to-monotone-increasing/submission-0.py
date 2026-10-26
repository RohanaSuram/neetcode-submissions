class Solution:
    def minFlipsMonoIncr(self, s: str):
        ones = 0
        flip = 0
        best = 0
        for i in s:
            if i == '1':
                ones += 1
            else:
                best = min(best + 1, ones)
        
        return best
        
