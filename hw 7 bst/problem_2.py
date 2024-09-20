class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # ------------------------------- queue methods -------------------------------
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def __str__(self):
        result = []
        curNode = self._head
        while curNode is not None:
            result.append(str(curNode._element) + " --> ")
            curNode = curNode._next
        result.append("None")
        return "".join(result)


class Tree:
    class TreeNode:
        def __init__(self, element, parent=None, left=None, right=None):
            self._parent = parent
            self._element = element
            self._left = left
            self._right = right

    # -------------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # -------------------------- public accessors ---------------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def is_root(self, node):
        """Return True if a given node represents the root of the tree."""
        return self._root == node

    def is_leaf(self, node):
        """Return True if a given node does not have any children."""
        return self.num_children(node) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for node in self.nodes():  # use same order as nodes()
            yield node._element  # but yield each element

    def depth(self, node):
        """Return the number of levels separating a given node from the root."""
        if self.is_root(node):
            return 0
        else:
            return 1 + self.depth(self.parent(node))

    def _height1(self):  # works, but O(n^2) worst-case time
        """Return the height of the tree."""
        return max(self.depth(node) for node in self.nodes() if self.is_leaf(node))

    def _height2(self, node):  # time is linear in size of subtree
        """Return the height of the subtree rooted at the given node."""
        if self.is_leaf(node):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(node))

    def height(self, node=None):
        """Return the height of the subtree rooted at a given node.
        If node is None, return the height of the entire tree.
        """
        if node is None:
            node = self._root
        return self._height2(node)  # start _height2 recursion

    def nodes(self):
        """Generate an iteration of the tree's nodes."""
        return self.preorder()  # return entire preorder iteration

    def preorder(self):
        """Generate a preorder iteration of nodes in the tree."""
        if not self.is_empty():
            for node in self._subtree_preorder(self._root):  # start recursion
                yield node

    def _subtree_preorder(self, node):
        """Generate a preorder iteration of nodes in subtree rooted at node."""
        yield node  # visit node before its subtrees
        for c in self.children(node):  # for each child c
            for other in self._subtree_preorder(c):  # do preorder of c's subtree
                yield other  # yielding each to our caller

    def postorder(self):
        """Generate a postorder iteration of nodes in the tree."""
        if not self.is_empty():
            for node in self._subtree_postorder(self._root):  # start recursion
                yield node

    def _subtree_postorder(self, node):
        """Generate a postorder iteration of nodes in subtree rooted at node."""
        for c in self.children(node):  # for each child c
            for other in self._subtree_postorder(c):  # do postorder of c's subtree
                yield other  # yielding each to our caller
        yield node  # visit node after its subtrees

    def breadthfirst(self):
        """Generate a breadth-first iteration of the nodes of the tree."""
        if not self.is_empty():
            fringe = LinkedQueue()  # known nodes not yet yielded
            fringe.enqueue(self._root)  # starting with the root
            while not fringe.is_empty():
                node = fringe.dequeue()  # remove from front of the queue
                yield node  # report this node
                for c in self.children(node):
                    fringe.enqueue(c)  # add children to back of queue

    def root(self):
        """Return the root of the tree (or None if tree is empty)."""
        return self._root

    def parent(self, node):
        """Return node's parent (or None if node is the root)."""
        return node._parent

    def left(self, node):
        """Return node's left child (or None if no left child)."""
        return node._left

    def right(self, node):
        """Return node's right child (or None if no right child)."""
        return node._right

    def children(self, node):
        """Generate an iteration of nodes representing node's children."""
        if node._left is not None:
            yield node._left
        if node._right is not None:
            yield node._right

    def num_children(self, node):
        """Return the number of children of a given node."""
        count = 0
        if node._left is not None:  # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1
        return count

    def sibling(self, node):
        """Return a node representing given node's sibling (or None if no sibling)."""
        parent = node._parent
        if parent is None:  # p must be the root
            return None  # root has no sibling
        else:
            if node == parent._left:
                return parent._right  # possibly None
            else:
                return parent._left  # possibly None

    # -------------------------- nonpublic mutators --------------------------
    def add_root(self, e):
        """Place element e at the root of an empty tree and return the root node.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self.TreeNode(e)
        return self._root

    def add_left(self, node, e):
        """Create a new left child for a given node, storing element e in the new node.
        Return the new node.
        Raise ValueError if node already has a left child.
        """
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self.TreeNode(e, node)  # node is its parent
        return node._left

    def add_right(self, node, e):
        """Create a new right child for a given node, storing element e in the new node.
        Return the new node.
        Raise ValueError if node already has a right child.
        """
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self.TreeNode(e, node)  # node is its parent
        return node._right

    def _replace(self, node, e):
        """Replace the element at given node with e, and return the old element."""
        old = node._element
        node._element = e
        return old

    def _attach(self, node, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external node.
        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if node already has a child. (This operation requires a leaf node!)
        """
        if not self.is_leaf(node):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():  # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None  # set t2 instance to empty
            t2._size = 0


class BinarySearchTree(Tree):

    # ------------------------------- nonpublic utilities -------------------------------
    def _subtree_search(self, node, v):
        """Return the node having value v, or last node searched."""
        if v == node._element:  # found match
            return node
        elif v < node._element:  # search left subtree
            if node._left is not None:
                return self._subtree_search(node._left, v)
        else:  # search right subtree
            if node._right is not None:
                return self._subtree_search(node._right, v)
        return node  # unsucessful search

    def _subtree_first_position(self, node):
        """Return the node that contains the first item in subtree rooted at given node."""
        walk = node
        while walk._left is not None:  # keep walking left
            walk = walk._left
        return walk

    def _subtree_last_position(self, node):
        """Return the node that contains the last item in subtree rooted at given node."""
        walk = node
        while walk._right is not None:  # keep walking right
            walk = walk._right
        return walk

    # --------------------- public methods providing Binary Search Tree support ---------------------
    def first(self):
        """Return the first node (smallest node) in the tree (or None if empty)."""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last node (largest node) in the tree (or None if empty)."""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, node):
        """Return the node that is just before the given node in the natural order.
        Return None if the given node is the first position.
        """
        if node._left is not None:
            return self._subtree_last_position(node._left)
        else:
            # walk upward
            walk = node
            above = walk._parent
            # Keeping looking for the first encountered smaller value from ancestor. Either way will work
            # Either way will work
            # while above is not None and walk == above._left:
            while above is not None and above._element > walk._element:
                walk = above
                above = walk._parent
            return above

    def after(self, node):
        """Return the node that is just after the given node in the natural order.
        Return None if the given node is the last position.
        """
        if node._right is not None:
            return self._subtree_first_position(node._right)
        else:
            walk = node
            above = walk._parent
            # Keeping looking for the first encountered larger value from ancestor. Either way will work
            # while above is not None and walk == above._right:
            while above is not None and above._element < walk._element:
                walk = above
                above = walk._parent
            return above

    # --------------------- public methods for accessing/mutating ---------------------
    def get_node(self, v):
        """Return the node associated with value (raise Error if not found)."""
        if self.is_empty():
            raise ValueError('Tree is empty')
        else:
            node = self._subtree_search(self._root, v)
            if v != node._element:
                raise ValueError('Not found: ' + repr(v))
            return node

    def insert(self, v):
        """Insert value v into the Binary Search Tree"""
        if self.is_empty():
            leaf = self.add_root(v)  # from BinaryTree (class Tree)
        else:
            node = self._subtree_search(self._root, v)
            if node._element < v:
                leaf = self.add_right(node, v)  # inherited from BinaryTree (class Tree)
            else:
                leaf = self.add_left(node, v)  # inherited from BinaryTree (class Tree)

    def __iter__(self):
        """Generate an iteration of all values in order."""
        node = self.first()
        while node is not None:
            yield node._element
            node = self.after(node)

    def __reversed__(self):
        """Generate an iteration of all values in reverse order."""
        node = self.last()
        while node is not None:
            yield node._element
            node = self.before(node)

    def delete_range(self, start, end):
        # Please write your code here
        if self.is_empty():
            return
        stack, node = [], self._root

        while node or stack:
            if node:
                stack.append(node)
                node = node._left
            else:
                node = stack.pop()
                self._delete_node(node) if start <= node._element <= end else None
                node = node._right if node._element <= end else node._left

    def _delete_node(self, node):
        parent = node._parent

        if not node._left and not node._right:
        # Node has no children, simply remove it
            if parent:
                setattr(parent, '_left' if parent._left == node else '_right', None)
        elif node._left and node._right:
            # Node has two children, replace it with the in-order successor
            successor = self._subtree_first_position(node._right)
            node._element, successor._element = successor._element, node._element
            self._delete_node(successor)
        else:
            # Node has one child, replace it with the child
            child = node._left or node._right
            if child:
                child._parent = parent
            setattr(self, '_root', child) if parent is None else setattr(parent, '_left' if parent._left == node else '_right', child)

        self._size -= 1


def main():
    bst = BinarySearchTree()

    bst.insert(18)
    bst.insert(6)
    bst.insert(21)
    bst.insert(24)
    bst.insert(1)
    bst.insert(9)
    bst.insert(0)
    bst.insert(4)
    bst.insert(10)
    bst.insert(14)
    bst.insert(12)
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)

    print("Before deletion:")
    print(list(bst))  # [0, 1, 2, 3, 4, 5, 6, 9, 10, 12, 14, 18, 21, 24]

    bst.delete_range(5, 10)

    print("After deletion:")
    print(list(bst))  # [0, 1, 2, 3, 4, 12, 14, 18, 21, 24]


if __name__ == '__main__':
    main()

