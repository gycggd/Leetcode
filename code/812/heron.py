from math import sqrt
class Solution:
    def largestTriangleArea(self, points):
        dist = {}
        def d(p1, p2):
            return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        N = len(points)
        for i in range(N):
            for j in range(i+1, N):
                if i not in dist:
                    dist[i] = {}
                dist[i][j] = d(points[i], points[j])
        ret = 0
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    p1, p2, p3 = dist[i][j], dist[j][k], dist[i][k]
                    p = (p1+p2+p3)/2
                    ret = max(ret, sqrt(max(p*(p-p1)*(p-p2)*(p-p3), 0)))
        return ret