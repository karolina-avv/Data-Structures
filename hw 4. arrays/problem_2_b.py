def union(l1, l2):
    """
       This function returns the union of lists l1 and l2
    """
    common = []
    for item in l1:
        if item not in l2:
            common.append(item)
    common += l2
    return common

def main():
    l1 = [1, 3, 5, 7, 9]
    l2 = [3, 4, 5, 6, 7]

    l = union(l1, l2)
    l.sort()
    print(l)  # should print [1, 3, 4, 5, 6, 7, 9]


if __name__ == '__main__':
    main()
