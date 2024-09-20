class Node:
    """
        Lightweight, nonpublic class for storing a doubly linked node.
    """

    def __init__(self, element=None, prev=None, next=None):  # initialize node’s fields
        self._element = element  # user’s element
        self._prev = prev  # previous node reference
        self._next = next  # next node reference


class DoubleLinkedList:
    def __init__(self):
        """
            Create an empty DoubleLinkedList.
            You can also modify this function if needed
        """
        self._header = Node(None, None, None)
        self._trailer = Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """
            Return the number of elements in the DoubleLinkedList.
        """
        return self._size

    def is_empty(self):
        """
            Return True if the DoubleLinkedList is empty.
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def __str__(self):
        result = "Header<-->"
        currNode = self._header._next
        while currNode is not self._trailer:
            result += str(currNode._element) + "<-->"
            currNode = currNode._next
        return result + "Trailer"

    def insertAtFirst(self, e):
        self._insert_between(e, self._header, self._header._next)

    def shuffle(self):
        self._size = self._size
        self._header = self._header
        half1 = self._header._next
        self._trailer = self._trailer
        half2 = self._trailer._prev
        half = self._size // 2

        i = 0
        while i < half:
            temp2, half2._prev = half2._prev, half1
            temp2._next, self._trailer._prev = self._trailer, temp2

            temp1 = half1._next
            half1._next, temp1._prev, half2._next = half2, half2, temp1

            half1 = temp1
            half2 = temp2

            i += 1
            if i >= half:
                break
        
def main():
    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(4)
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(1)

    print(ls1)  # Should print: Header<-->1<-->2<-->3<-->4<-->Trailer
    ls1.shuffle()
    print(ls1)  # Should print: Header<-->1<-->4<-->2<-->3<-->Trailer


if __name__ == '__main__':
    main()
