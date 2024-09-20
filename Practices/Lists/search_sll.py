#search for a given value in a singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def search_sll(self, target):
        current= self.head
        while current is not None:
            if current== target:
                return True
            else:
                current= current._next

        return False

if __name__ == "__main__":
    # Create a singly linked list
    linked_list = LinkedList()

    # Insert nodes into the linked list (code for insertion not provided in the skeleton)
    # ...

target_value = 42
if linked_list.search_sll(target_value):
    print(f"{target_value} found in the linked list.")
else:
    print(f"{target_value} not found in the linked list.")
    
