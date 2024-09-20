def sort_enchanted_trees(tree_values):
    #use insertion sort- start empty, insert and compare with the hand's items
    #O(n^2)
    #left side: sorted
    #right side: not yet sorted goal is to have everything on left hand

    for i in range(1, len(tree_values)):
        j = i
        while j > 0 and tree_values[j] < tree_values[j - 1]:
            tree_values[j], tree_values[j - 1] = tree_values[j - 1], tree_values[j]
            j -= 1

    return tree_values

def main():
    tree_values = [30, 20, 40, 10, 50, 15, 35, 25, 45]
    sorted_trees = sort_enchanted_trees(tree_values)
    print(sorted_trees)  # should print [10, 15, 20, 25, 30, 35, 40, 45, 50]


if __name__ == '__main__':
    main()
