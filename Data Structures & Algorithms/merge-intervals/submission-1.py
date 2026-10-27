class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = []
        prev = intervals[0]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= prev[1]:
                prev = [prev[0], max(prev[1], curr[1])]
            else:
                output.append(prev)
                prev = curr
        
        output.append(prev)
        return output

           
        