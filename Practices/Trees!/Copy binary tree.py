#copy binary tree

class TreeWithParent:
    def __init__(self, element, left=None, right=None, parent= None):
        self._element= element
        self._left= left
        self._right= right
        self._parent= parent
        
    def copy(node):
        if not node:
            return None

        copied_tree= TreeWithParent(node._element, parent= node._parent)
        copied_tree._left= self.copy(node._left)
        copied_tree._right= self.copy(node._right)

        if copied_tree._left is not None:
            copied_tree._left._parent= copied_tree

        if coped_tree._right is not None:
            copied_tree._right._parent= copied_tree

        return copied_tree

def main():
    tree= TreeWithParent()
    tree._left= TreeWithParent(2, parent=tree)
    tree._right= TreeWithParent(4, parent=tree)
    tree._left._left= TreeWithParent(5, parent=tree._left)
    tree._right._left= TreeWithParent(7, parent=tree._right)
    tree._left._left._left= TreeWithParent(3, parent=tree._left._left)
    tree._left._left._right= TreeWithParent(6, parent=tree._left._left)


    tree2= copy(tree)
    print(tree2)

if __name__== "__main__":
    main()
        
        
