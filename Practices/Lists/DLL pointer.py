class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def rearrange(poi):
    if poi is None or poi.next is None or poi.prev is None:
            return None

    left_node= poi.prev
    right_node= poi.next

    while left_node is not None and right_node is not None:
        left_node, right_node.next= right_node.next, left_node
        left_node.prev, right_node= right_node, left_node.prev
        
        left_node= left_node.prev
        right_node= right_node.next

    return poi
            
def print_dll(header):
    current = header.next
    while current is not None:
        print(current.data, end=" <-> " if current.next is not None else "\n")
        current = current.next

def main():
    # Create a doubly linked list: Header <-> 1 <-> 2 <-> 3 <-> A <-> B <-> C <-> Trailer
    header = Node("Header")
    trailer = Node("Trailer")
    header.next = Node(1)
    header.next.prev = header
    header.next.next = Node(2)
    header.next.next.prev = header.next
    header.next.next.next = Node(3)
    header.next.next.next.prev = header.next.next
    header.next.next.next.next = Node('A')
    header.next.next.next.next.prev = header.next.next.next
    header.next.next.next.next.next = Node('B')
    header.next.next.next.next.next.prev = header.next.next.next.next
    header.next.next.next.next.next.next = Node('C')
    header.next.next.next.next.next.next.prev = header.next.next.next.next.next
    header.next.next.next.next.next.next.next = trailer
    trailer.prev = header.next.next.next.next.next.next

    print("Original DLL:")
    print_dll(header)

    # Call rearrange function on the node 'A'
    poi = header.next.next.next.next
    rearrange(poi)

    print("\nDLL after rearranging around 'A':")
    print_dll(header)

if __name__ == "__main__":
    main()
