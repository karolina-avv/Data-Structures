#flatten list using recursion

def flatten(l):
    x= []
    for i in l:
        if isinstance(i, list):
            x.extend(flatten(i))
        else:
            x.append(i)

    return x


def main():
    nested_list = [1, 2, [3, 4, [5, 6]], 7, [8]]
    flattened_list = flatten(nested_list)
    print("Original Nested List:")
    print(nested_list)
    print("Flattened List:")
    print(flattened_list)

if __name__ == "__main__":
    main()
