def rotator(M, a, d):
    """
        a in {0, 90, 180}
        d in {"clockwise","anticlockwise"}
        You should not change the value of M in this function.
    """
    if a == 0:
        return M

    rows= len(M)
    cols = len(M[0])
    new_M = [[0] * rows for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if a == 90:
                if d == 'clockwise':
                    new_M[c][rows - 1 - r] = M[r][c]
                else:
                    new_M[cols - 1 - c][r] = M[r][c]
            elif a == 180:
                new_M[rows - 1 - r][cols - 1 - c] = M[r][c]

    return new_M


def main():
    mat = [ [ 1, 2, 3, 4, 5], \
            [ 6, 7, 8, 9,10], \
            [11,12,13,14,15], \
            [16,17,18,19,20], \
            [21,22,23,24,25] ]
    new_mat = rotator(mat,90,"anticlockwise")
    print(new_mat)
    # should print [ [ 5,10,15,20,25], \
            #        [ 4, 9,14,19,24], \
            #        [ 3, 8,13,18,23], \
            #        [ 2, 7,12,17,22], \
            #        [ 1, 6,11,16,21] ]
    new_mat = rotator(mat,0,"anticlockwise")
    print(new_mat)
    # should print [ [ 1, 2, 3, 4, 5], \
            #        [ 6, 7, 8, 9,10], \
            #        [11,12,13,14,15], \
            #        [16,17,18,19,20], \
            #        [21,22,23,24,25] ]


if __name__ == '__main__':
    main()