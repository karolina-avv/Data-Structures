def intersect(l1, l2):
    """
       This function returns the intersection of lists l1 and l2
    """
    common = []    
    for item in l1:
        if item in l2:
            common.append(item)

    return common

def main():
    l1 = [1, 3, 5, 7, 9]
    l2 = [3, 4, 5, 6, 7]

    l = intersect(l1, l2)
    l.sort()
    print(l)  # should print [3, 5, 7]


if __name__ == '__main__':
    main()
