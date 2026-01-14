class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = set()

        # Build sweep line events
        for x, y, l in squares:
            events.append((y, 1, x, x + l))      # enter
            events.append((y + l, -1, x, x + l)) # exit
            xs.add(x)
            xs.add(x + l)

        xs = sorted(xs)
        x_id = {x: i for i, x in enumerate(xs)}

        class SegmentTree:
            def __init__(self, n):
                self.count = [0] * (4 * n)
                self.covered = [0] * (4 * n)

            def update(self, node, l, r, ql, qr, val):
                if ql >= r or qr <= l:
                    return
                if ql <= l and r <= qr:
                    self.count[node] += val
                else:
                    mid = (l + r) // 2
                    self.update(node * 2, l, mid, ql, qr, val)
                    self.update(node * 2 + 1, mid, r, ql, qr, val)

                if self.count[node] > 0:
                    self.covered[node] = xs[r] - xs[l]
                else:
                    if r - l == 1:
                        self.covered[node] = 0
                    else:
                        self.covered[node] = (
                            self.covered[node * 2] +
                            self.covered[node * 2 + 1]
                        )

        events.sort()
        st = SegmentTree(len(xs) - 1)

        # First pass: compute total union area
        total_area = 0.0
        prev_y = events[0][0]

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            total_area += st.covered[1] * dy
            st.update(1, 0, len(xs) - 1, x_id[x1], x_id[x2], typ)
            prev_y = y

        half = total_area / 2.0

        # Second pass: find minimum y where area reaches half
        st = SegmentTree(len(xs) - 1)
        curr_area = 0.0
        prev_y = events[0][0]

        for y, typ, x1, x2 in events:
            dy = y - prev_y
            area_add = st.covered[1] * dy

            if curr_area + area_add >= half:
                return prev_y + (half - curr_area) / st.covered[1]

            curr_area += area_add
            st.update(1, 0, len(xs) - 1, x_id[x1], x_id[x2], typ)
            prev_y = y

        return prev_y
