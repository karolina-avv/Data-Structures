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
        while currNode is not self._trailer and currNode is not None:
            result += str(currNode._element) + "<-->"
            currNode = currNode._next
        return result + "Trailer"

    def insertAtFirst(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def partition_list(self, pivot):
        current = self._header._next
        left_header = Node(None, None, None)
        right_header = Node(None, None, None)
        left_tail = left_header
        right_tail = right_header

        while current is not self._trailer:
            next_node = current._next
            if current._element < pivot:
                left_tail._next = current
                left_tail = current
            else:
                right_tail._next = current
                right_tail = current
            current = next_node

        left_tail._next = right_header._next
        if right_header._next:
            right_header._next._prev = left_tail

        self._header._next, left_header._next._prev = left_header._next, self._header
        self._trailer._prev, right_tail._next = right_tail, self._trailer   
            
                    


def main():
    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(4)
    ls1.insertAtFirst(8)
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(7)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(6)
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(5)

    print(ls1)  # Should print: Header<-->5<-->1<-->6<-->2<-->7<-->3<-->8<-->4<-->Trailer
    ls1.partition_list(5)
    print(ls1)  # Should print: Header<-->1<-->2<-->3<-->4<-->5<-->6<-->7<-->8<-->Trailer

    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(4)
    ls1.insertAtFirst(8)
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(7)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(6)
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(5)

    print(ls1)  # Should print: Header<-->5<-->1<-->6<-->2<-->7<-->3<-->8<-->4<-->Trailer
    ls1.partition_list(3)
    print(ls1)  # Should print: Header<-->1<-->2<-->3<-->5<-->6<-->7<-->8<-->4<-->Trailer


if __name__ == '__main__':
    main()
