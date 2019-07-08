def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

if __name__ == '__main__':
    for xs in [(0, 0),(1, 0),(0, 1),(1, 1)]:
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))