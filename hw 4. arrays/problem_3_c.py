def rotator(M,a,d):
    """
        a in {0, 90, 180}
        d in {"clockwise","anticlockwise"}
        You should change the value of M in this function
    """

    if a == 0:
        return M
    

    elif a == 180:
        for r in range(5):
            for c in range(5):
                if r + c < 4:
                    M[r][c], M[4 - r][4 - c] = M[4 - r][4 - c], M[r][c]
        M[0][4], M[4][0] = M[4][0], M[0][4]
        M[1][3], M[3][1] = M[3][1], M[1][3]

    else:
        for r in range(len(M)//2 + 1):
            for c in range(r, len(M[0]) - r - 1):
                if d == 'clockwise':
                    M[r][c], M[c][4-r], M[4-r][4-c], M[4-c][r] = M[4-c][r], M[r][c], M[c][4-r], M[4-r][4-c]
                else:
                    M[r][c], M[c][4-r], M[4-r][4-c], M[4 - c][r] = M[c][4-r], M[4-r][4-c], M[4-c][r], M[r][c]


    return M



def main():
    mat = [ [ 1, 2, 3, 4, 5], \
            [ 6, 7, 8, 9,10], \
            [11,12,13,14,15], \
            [16,17,18,19,20], \
            [21,22,23,24,25] ]
    rotator(mat,90,"anticlockwise")
    print(mat)
    # should print [ [ 5,10,15,20,25], \
            #        [ 4, 9,14,19,24], \
            #        [ 3, 8,13,18,23], \
            #        [ 2, 7,12,17,22], \
            #        [ 1, 6,11,16,21] ]
    rotator(mat,0,"anticlockwise")
    print(mat)
    # should print [ [ 5,10,15,20,25], \
            #        [ 4, 9,14,19,24], \
            #        [ 3, 8,13,18,23], \
            #        [ 2, 7,12,17,22], \
            #        [ 1, 6,11,16,21] ]


if __name__ == '__main__':
    main()