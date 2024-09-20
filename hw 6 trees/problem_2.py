class Empty(Exception):
    pass

class LinkQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    __slots__ = "_head", "_tail", "_size"

    class _Node:
        """Lightweight,nonpublic class for storing a singly linked node."""
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is emtpy."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue.
        Raise Emtpy exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, item):
        """Add an element to the back of queue."""
        newest = self._Node(item, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


class Tree:
    """Abstract base class representing a tree structure."""

    # ----------------------------nested Position class -----------------------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """return the element stored at this Position"""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    # ---------- abstract methods that concrete subclass must support------------

    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent """
        return NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass")

    # --------------------- concrete methods implemented in this class --------------
    def is_root(self, p):
        "Return True if Position p represents the root of the tree."
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.
        If p is None,return height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():
            yield p.element()

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of position in subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.breadthfirst()

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of thr tree."""
        if self.is_empty():
            raise Empty("tree is None")
        else:
            queue = LinkQueue()
            queue.enqueue(self.root())
            while len(queue) != 0:
                node = queue.dequeue()
                yield node
                for children in self.children(node):
                    queue.enqueue(children)


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # -------------------additional abstract methods -------------------------
    def left(self, p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        raise NotImplementedError("must be implemented by subclass")

    # ----------------------------concrete  methods implemented in this class ===========
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)。"""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteraiton of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """Linked representation of binary tree structure."""

    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree):
        """ An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node ,if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # ------------------------ binary tree constructor --------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # --------------------public accessors ---------------------
    def __len__(self):
        """return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree(or None if tree is empty)"""
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError("Root exists")
        self._size += 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p,storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists.")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p,storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at position p with e , and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p , and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    def _delete_subtree(self, p):
        linkqueue = LinkQueue()
        linkqueue.enqueue(p)
        while len(linkqueue) != 0:
            node = linkqueue.dequeue()
            print(node.element(), end=' ')
            for children in self.children(node):
                linkqueue.enqueue(children)
            node._node._parent = node._node._left = node._node._right = node._node._element = None

    def _swap(self, e, q):
        # Time complexity requirement: O(1)
        # Space complexity requirement: O(1)
        node_e = self._validate(e)
        node_q = self._validate(q)

        if node_e is None or node_q is None:
            return

        node_e_parent = node_e._parent
        node_q_parent = node_q._parent

        node_e_left = node_e._left
        node_e_right = node_e._right

        node_q_left = node_q._left
        node_q_right = node_q._right

        if node_e_parent is not None:
            if node_e_parent._left == node_e:
                node_e_parent._left = node_q
            else:
                node_e_parent._right = node_q
        else:
            self._root = node_q

        if node_q_parent is not None:
            if node_q_parent._left == node_q:
                node_q_parent._left = node_e
            else:
                node_q_parent._right = node_e
        else:
            self._root = node_e

    # Swap the left and right child references
        if node_e_left and node_e_left != node_q:
            node_e_left._parent = node_q
        node_e._left = node_q_left if node_q_left and node_q_left != node_e else node_q

        if node_q_left and node_q_left != node_e:
            node_q_left._parent = node_e
        node_q._left = node_e_left if node_e_left and node_e_left != node_q else node_e

        if node_e_right and node_e_right != node_q:
            node_e_right._parent = node_q
        node_e._right = node_q_right if node_q_right and node_q_right != node_e else node_q

        if node_q_right and node_q_right != node_e:
            node_q_right._parent = node_e
        node_q._right = node_e_right if node_e_right and node_e_right != node_q else node_e


def main():
    tree = LinkedBinaryTree()
    root = tree._add_root("Providence")
    left = tree._add_left(root, "Chicago")
    right = tree._add_right(root, "Seattle")
    tree._add_left(left, "Baltimore")
    tree._add_right(left, "New York")

    id_root_old = id(tree.root()._node)
    print(id_root_old, tree.root().element())  # should print <memory id> "Providence"
    id_left_old = id(tree.left(tree.root())._node)
    tree._swap(root, left)  # swap root and left node
    id_root_new = id(tree.root()._node)
    id_left_new = id(tree.left(tree.root())._node)

    print(id_root_new, tree.root().element())  # should print <memory id> "Chicago"

    print(id_root_old == id_left_new and id_root_new == id_left_old)  # should print true


if __name__ == '__main__':
    main()
