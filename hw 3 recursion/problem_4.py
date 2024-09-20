def throw_stones(N, M):
#helper function using recursion
    def throw_recursive(N, M, current_throw=()):
        #base when thrown everything
        if N == 0 and M == 0:
            return [current_throw]
        if N < 0 or M <= 0:
            return []

        #list storing combinations
        ways = []

        #recursion to find possible combinations
        if M % 2 == 0:
            ways.extend(throw_recursive(N - 3, M - 1, current_throw + (3,))) if N >= 3 else None
            ways.extend(throw_recursive(N - 1, M - 1, current_throw + (1,))) if N >= 1 else None
        else:
            ways.extend(throw_recursive(N - 3, M - 1, current_throw + (3,))) if N >= 3 else None
            ways.extend(throw_recursive(N - 2, M - 1, current_throw + (2,))) if N >= 2 else None
            ways.extend(throw_recursive(N - 1, M - 1, current_throw + (1,))) if N >= 1 else None

        return ways

    return throw_recursive(N, M, ())

def main():
    print(throw_stones(5, 3))  # Expect: [(1, 1, 3), (1, 3, 1), (2, 1, 2), (3, 1, 1)] or [[1, 1, 3], [1, 3, 1], [2, 1, 2], [3, 1, 1]]
    print(throw_stones(6, 2))  # Expect: [(3, 3)] or [[3, 3]]


if __name__ == '__main__':
    main()
