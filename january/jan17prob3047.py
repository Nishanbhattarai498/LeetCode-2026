class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0

        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i + 1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                # Calculate intersection
                left = max(x1, x3)
                right = min(x2, x4)
                bottom = max(y1, y3)
                top = min(y2, y4)

                if left < right and bottom < top:
                    side = min(right - left, top - bottom)
                    max_area = max(max_area, side * side)

        return max_area