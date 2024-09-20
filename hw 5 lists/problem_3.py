class Node:
    def __init__(self, element=None, next=None):
        self._element = element
        self._next = next


class SinglyLinkedList:
    def __init__(self):
        """Create an empty LinkedList."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the LinkedList."""
        return self._size

    def is_empty(self):
        """Return True if the LinkedList is empty."""
        return self._size == 0

    def insertAtFirst(self, e):
        """Add element e to the start of the LinkedList."""
        newNode = Node(e, self._head)
        self._head = newNode
        self._size += 1

    def deleteFirst(self):
        """Remove and return the first element from the LinkedList.
        Raise Empty exception if the Linked list is empty.
        Return: the value of the first node
        """
        if self.is_empty():
            raise Exception('LinkedList is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def deleteLast(self):
        """Remove and return the last element from the LinkedList.
        Raise Empty exception if the Linked list is empty.
        Return: the value of the last node
        """
        if self.is_empty():
            raise Exception('LinkedList is empty')
        prv = None
        cur = self._head
        while cur._next is not None:
            cur = cur._next
            prv = prv._next if prv is not None else self._head
        if prv is None:
            self._head = None
        else:
            prv._next = None
        self._size -= 1
        return cur._element

    def unOrderedSearch(self, target):
        currNode = self._head
        while currNode is not None and currNode._element != target:
            currNode = currNode._next
        return currNode is not None

    def __str__(self):
        current = self._head
        elements = []
        while current:
            elements.append(current._element)
            current = current._next

        elements.sort(key=lambda x: x[0])
        elements_str = "Head-->" + "-->".join(map(str, elements)) + "-->None"
        return elements_str


class FavSinglyLinkedList:
    def __init__(self):
        self._data = SinglyLinkedList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        prev = None
        Curr = self._data._head

        while Curr:
            if Curr._element[0] == e:
                Curr._element[1] += 1
                if prev:
                    prev._next = Curr._next
                    Curr._next = self._data._head
                    self._data._head = Curr
                return

            prev, Curr = Curr, Curr._next

        new = Node([e, 1])
        new._next, self._data._head = self._data._head, new

    def __str__(self):
        return str(self._data)


def main():
    d = FavSinglyLinkedList()
    for i in range(10):
        d.access('www.a')
        if i % 2 == 0:
            d.access('www.b')
        if i % 3 == 0:
            d.access('www.c')
        if i % 5 == 0:
            d.access('www.d')
    print(d)  # Expect "Head-->['www.a', 10]-->['www.b', 5]-->['www.c', 4]-->['www.d', 2]-->None"


if __name__ == '__main__':
    main()
