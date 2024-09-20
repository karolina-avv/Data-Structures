def solver(f, low, high):
   #binary search finding of root between low and high
    if f(low) == 0:
        return low
    if f(high) == 0:
        return high

    while low != high:
        mid = (low + high) / 2
        if f(mid) == 0:
            return mid

        if f(mid) * f(low) < 0:
            high = mid
        else:
            low = mid

    return (low + high) / 2

def main():
    f1 = lambda x: x - 1  # f(x) = x - 1
    f2 = lambda x: x ** 3 - 100 * x ** 2 - x + 100  # f(x) = x^3 - 100x^2 - x + 100

    x = solver(f1, -50, 60)
    print(x)  # should be one of [1.0]

    x = solver(f2, 0, 2)
    print(x)  # should be one of [-1, 1, 100]


if __name__ == '__main__':
    main()