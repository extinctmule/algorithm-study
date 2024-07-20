X = "ABCBDAB"
Y = "BDCABA"


def lcs(x, y):

    if not x or not y:
        return ""

    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        a, b = lcs(x[:-1], y), lcs(x, y[:-1])
        if len(a) >= len(b):
            return a
        else:
            return b


# res=""
print(lcs(X, Y))
