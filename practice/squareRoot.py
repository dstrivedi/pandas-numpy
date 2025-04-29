def squareRoot(n):
    est = n / 2
    while True:
        print(est)
        y = (est + n/est) / 2
        if y == est:
            break
        est = y
    # return est

squareRoot(256)
squareRoot(144)