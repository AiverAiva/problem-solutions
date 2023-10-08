# runtime: Beats 96.71%of users with Python
# memory: Beats 97.12%of users with Python
# lol

class Solution(object):
    def maxPoints(self, points):
        if len(points) < 3: return len(points)
        result=2
        for i in range(len(points)):
            p1 = points[i]
            data = {}
            for p2 in points[i+1:]:
                a = None
                x = p2[0] - p1[0]
                if x:
                    a = (1.0*p2[1] - p1[1]) / x
                if a in data:
                    new = data[a] = data[a] + 1
                    if new > result:
                        result = new
                else:
                    data[a] = 2
        return result

        """
        :type points: List[List[int]]
        :rtype: int
        """
        