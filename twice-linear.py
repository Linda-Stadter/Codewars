import math


def dbl_linear(n):
    res = [1, 3]
    p2 = 1
    p3 = 0

    while p2 < n and p3 < n:
        y = res[p2] * 2 + 1
        z = res[p3] * 3 + 1
        if z > y:
            p2 += 1
            res.append(y)
        elif z < y:
            p3 += 1
            res.append(z)
        else:
            p2 += 1

    return res[n]
    