    #remove duplicates from a list


class _Node:
    def __init__(self, element, prev, next):  # initialize node’s fields
        self._element = element  # user’s element
        self._prev = prev  # previous node reference
        self._next = next  # next node reference

    __slots__ = _element, _prev, _next  # streamline memory

    

class _DoublyLinkedBase:
    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        self._element = element  # user’s element


    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def remove_duplicates(self):
        current= self._header

        while (current._next != None):
            if current._element== current._element._next:
                self._delete_node(current._element)
            else:
                current= current._next

        return self._header
        
            

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(4)
    my_list.append(5)

    print("Original list:")
    my_list.display()

    my_list.remove_duplicates()
    print("List after removing duplicates:")
    my_list.display()
