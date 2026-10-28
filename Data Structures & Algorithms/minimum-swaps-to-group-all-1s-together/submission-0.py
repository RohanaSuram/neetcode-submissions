class Solution:
    def minSwaps(self, data: List[int]) -> int:
        pass
        slidingwindow = sum(data)
        ones = sum(data[:slidingwindow])
        maxones = ones

        for right in range(slidingwindow, len(data)):
            ones += data[right]
            ones -= data[right - slidingwindow]
            maxones = max(maxones, ones)
        return slidingwindow - maxones