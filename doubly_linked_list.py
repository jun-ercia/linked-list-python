class Node:
    """
    Represents a node in a Doubly Linked List.
    
    Attributes:
        data : Stores the value
        next : Reference to the next node
        prev : Reference to the previous node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Implementation of a Doubly Linked List (DLL).
    
    Supports:
    - Forward and backward traversal
    - Insertion at front and end
    - Deletion of nodes
    - Searching elements
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Returns True if the list is empty."""
        return self.head is None

    def search(self, data):
        """
        Searches for a value in the list.
        
        Returns:
            True if found, otherwise False
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def traverse_forward(self):
        """
        Traverses the list from head to tail.
        """
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        result = "Head -> "

        while current:
            result += f"{current.data} <-> "
            current = current.next

        result += "None"
        print(result)

    def traverse_backward(self):
        """
        Traverses the list from tail to head.
        """
        if self.is_empty():
            print("List is empty.")
            return

        # Move to last node
        current = self.head
        while current.next:
            current = current.next

        result = "Tail -> "

        while current:
            result += f"{current.data} <-> "
            current = current.prev

        result += "None"
        print(result)

    def insert_at_front(self, data):
        """
        Inserts a node at the beginning of the list.
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a node at the end of the list.
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            return

        current = self.head

        # Traverse to last node
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def delete(self, data):
        """
        Deletes the first occurrence of the given value.
        
        Returns:
            True if successful, otherwise False
        """
        if self.is_empty():
            print("Error: List is empty.")
            return False

        current = self.head

        while current:
            if current.data == data:

                # Case 1: Deleting the head node
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                # Case 2: Deleting middle or last node
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev

                print(f"{data} deleted successfully.")
                return True

            current = current.next

        print("Error: Value not found.")
        return False

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        current = self.head
        nodes = []

        while current:
            nodes.append(str(current.data))
            current = current.next

        return " <-> ".join(nodes) + " <-> None"


# ================= MAIN PROGRAM =================
def main():
    """
    Demonstrates Doubly Linked List operations.
    """

    dll = DoublyLinkedList()

    print("=== DOUBLY LINKED LIST DEMO ===\n")

    # ===== INSERTION =====
    print("Inserting elements at the end: 1, 2, 3")
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)

    print("Forward Traversal:")
    dll.traverse_forward()
    print()

    # ===== INSERT AT FRONT =====
    print("Inserting 0 at the front")
    dll.insert_at_front(0)

    print("Forward Traversal:")
    dll.traverse_forward()

    print("Backward Traversal:")
    dll.traverse_backward()
    print()

    # ===== SEARCH =====
    value = 2
    print(f"Searching for {value}...")
    print("Found\n" if dll.search(value) else "Not Found\n")

    # ===== DELETE =====
    delete_value = 3
    print(f"Deleting {delete_value}...")
    dll.delete(delete_value)

    print("After Deletion (Forward):")
    dll.traverse_forward()

    print("After Deletion (Backward):")
    dll.traverse_backward()
    print()

    # ===== FINAL DISPLAY =====
    print("Final List (using __str__):")
    print(dll)


# Entry point
if __name__ == "__main__":
    main()
