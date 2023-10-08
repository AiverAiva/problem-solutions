class Solution(object):
    def maximalRectangle(self, matrix):
        if matrix is None or len(matrix) < 1:
            return 0
        cols = len(matrix[0])
        height = [0] * (cols + 1)
        area = 0
        for row in matrix:
            for i in range(cols):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(cols + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    area = max(area, h * w)
                stack.append(i)
        return area
       
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        