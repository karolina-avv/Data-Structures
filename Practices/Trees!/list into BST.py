#list based binary search tree

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def convert(ls):
    def sorted_bst(start, end):
        if start> end:
            return None

        mid= (start + end) //2
        root= TreeNode(ls[mid])
        root.left= sorted_bst(start, mid-1)
        root.right= sorted_bst(mid+1, end)
        return root
    return sorted_bst(0, len(ls)-1)
            


def main():
    ls = [1, 2, 3, 4, 5, 6, 7]
    bst_root = convert(ls)
    inorder(bst_root)

if __name__ == "__main__":
    main()
