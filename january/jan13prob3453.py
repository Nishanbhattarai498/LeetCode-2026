class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0.0
        min_y = float('inf')
        max_y = float('-inf')

        # Compute total area and y-range
        for _, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        half = total_area / 2.0

        # Function to compute area below horizontal line y = h
        def area_below(h):
            area = 0.0
            for _, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += l * (h - y)
            return area

        low, high = min_y, max_y

        # Binary search for precise y-coordinate
        for _ in range(60):  # enough for 1e-5 precision
            mid = (low + high) / 2
            if area_below(mid) < half:
                low = mid
            else:
                high = mid

        return low