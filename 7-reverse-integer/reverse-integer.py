class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        if y[0] == '-':
            res = y[0]
            y1 = y[1:]
            d = res+y1[::-1]
            g = int(d)
            if g < -(2**31) or g > 2**31 - 1:
                return 0
            else:
                return g
        else:
            d = int(y[::-1])
            if d < -(2**31) or d > 2**31 - 1:
                return 0
            else:
                return d