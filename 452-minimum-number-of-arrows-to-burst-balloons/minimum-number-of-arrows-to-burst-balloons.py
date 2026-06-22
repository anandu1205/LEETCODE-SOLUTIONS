class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        res=[]
        res.append(points[0])
        for i in range(1,len(points)):
            if res[-1][1]>=points[i][0]:
                res[-1]=[max(res[-1][0],points[i][0]),min(res[-1][1],points[i][1])]
            else:
                res.append(points[i])
        return len(res)
        