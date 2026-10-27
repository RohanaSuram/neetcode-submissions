class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        totalarrows = len(points)
        currpoint = points[0]
        for i in range(1, len(points)):
            value = points[i]
            if currpoint[1] >= value[0]:
                currpoint = (value[0], min(currpoint[1],value[1]))
                totalarrows -= 1
            else:
                currpoint = value
        return totalarrows
