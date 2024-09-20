def deepest(lis):
    # find sublists within list
    sublists = [item for item in lis if isinstance(item, list)]

    # return list if there are no subs
    if not sublists:
        return lis

    # elements in sublists are integers
    if all(isinstance(item, int) for sublist in sublists for item in sublist):
        return sublists[0]

    # Recursively search for the deepest element within sublists
    return deepest([item for sublist in sublists for item in sublist])




def main():
    l1 = [[[1]]]
    l2 = [1, [2, [3]]]
    l3 = [[[1]], [2], [3]]

    print(deepest(l1))  # should print [1]
    print(deepest(l2))  # should print [3]
    print(deepest(l3))  # should print [1]


if __name__ == '__main__':
    main()
