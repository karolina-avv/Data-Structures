def mirror(M):
    """
       This function mirrors the square matrix
    """
    for row in M:
        row.reverse()


def main():
    mat = [[1, 2, 3, 4, 5], \
           [6, 7, 8, 9, 10], \
           [11, 12, 13, 14, 15], \
           [16, 17, 18, 19, 20], \
           [21, 22, 23, 24, 25]]
    mirror(mat)
    print(mat)
    # should print [ [ 5, 4, 3, 2, 1], \
    #        [10, 9, 8, 7, 6], \
    #        [15,14,13,12,11], \
    #        [20,19,18,17,16], \
    #        [25,24,23,22,21] ]
    mirror(mat)
    print(mat)
    # should print [ [ 1, 2, 3, 4, 5], \
    #        [ 6, 7, 8, 9,10], \
    #        [11,12,13,14,15], \
    #        [16,17,18,19,20], \
    #        [21,22,23,24,25] ]


if __name__ == '__main__':
    main()