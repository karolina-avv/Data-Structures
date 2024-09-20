def unique(lst, i=0):
    #base where all elements have been checked
    if i >= len(lst) - 1:
        return True

    #if any element equal then return False because not unique
    if any(lst[j] == lst[i] for j in range(i + 1, len(lst))):
        return False

    #recursion to check next element
    return unique(lst, i + 1)

def main():
    print(unique([1, 54, 3, 25, 39, 25, 2]))  # should print False
    print(unique([9, "a", [], [[35, 2], ["NYU"]], (100,)]))  # should print True


if __name__ == '__main__':
    main()
