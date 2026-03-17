class Node:
    """
    Represents a node in a Circular Doubly Linked List.
    
    Attributes:
        data : Stores the value
        next : Reference to the next node
        prev : Reference to the previous node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    """
    Implementation of a Circular Doubly Linked List (CDLL).

    In this structure:
    - The last node's next points to the head
    - The head's prev points to the last node
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Returns True if the list is empty."""
        return self.head is None

    def search(self, data):
        """
        Searches for a value in the circular list.
        Returns True if found, otherwise False.
        """
        if self.is_empty():
            return False

        current = self.head

        while True:
            if current.data == data:
                return True
            current = current.next

            if current == self.head:
                break

        return False

    def traverse_forward(self):
        """
        Traverses the list from head forward.
        """
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        result = "Head -> "

        while True:
            result += f"{current.data} <-> "
            current = current.next

            if current == self.head:
                break

        result += "(back to Head)"
        print(result)

    def traverse_backward(self):
        """
        Traverses the list from tail backward.
        """
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head.prev  # Start from tail
        result = "Tail -> "

        while True:
            result += f"{current.data} <-> "
            current = current.prev

            if current == self.head.prev:
                break

        result += "(back to Tail)"
        print(result)

    def insert_at_front(self, data):
        """
        Inserts a node at the beginning of the circular list.
        """
        new_node = Node(data)

        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return

        tail = self.head.prev

        new_node.next = self.head
        new_node.prev = tail

        tail.next = new_node
        self.head.prev = new_node

        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a node at the end of the circular list.
        """
        new_node = Node(data)

        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            return

        tail = self.head.prev

        new_node.next = self.head
        new_node.prev = tail

        tail.next = new_node
        self.head.prev = new_node

    def delete(self, data):
        """
        Deletes the first occurrence of the given value.
        Returns True if successful, otherwise False.
        """
        if self.is_empty():
            print("Error: List is empty.")
            return False

        current = self.head

        while True:
            if current.data == data:

                # Case 1: Only one node
                if current.next == self.head and current.prev == self.head:
                    self.head = None

                else:
                    # Adjust pointers
                    current.prev.next = current.next
                    current.next.prev = current.prev

                    # If deleting head, move head forward
                    if current == self.head:
                        self.head = current.next

                print(f"{data} deleted successfully.")
                return True

            current = current.next

            if current == self.head:
                break

        print("Error: Value not found.")
        return False

    def __str__(self):
        """
        Returns a string representation of the circular list.
        """
        if self.is_empty():
            return "List is empty."

        current = self.head
        nodes = []

        while True:
            nodes.append(str(current.data))
            current = current.next

            if current == self.head:
                break

        return " <-> ".join(nodes) + " <-> (back to Head)"


# ================= MAIN PROGRAM =================
def main():
    """
    Demonstrates Circular Doubly Linked List operations.
    """

    cdll = CircularDoublyLinkedList()

    print("=== CIRCULAR DOUBLY LINKED LIST DEMO ===\n")

    # ===== INSERTION =====
    print("Inserting elements at the end: 1, 2, 3")
    cdll.insert_at_end(1)
    cdll.insert_at_end(2)
    cdll.insert_at_end(3)

    print("Forward Traversal:")
    cdll.traverse_forward()

    print("Backward Traversal:")
    cdll.traverse_backward()
    print()

    # ===== INSERT AT FRONT =====
    print("Inserting 0 at the front")
    cdll.insert_at_front(0)

    print("Forward Traversal:")
    cdll.traverse_forward()

    print("Backward Traversal:")
    cdll.traverse_backward()
    print()

    # ===== SEARCH =====
    value = 2
    print(f"Searching for {value}...")
    print("Found\n" if cdll.search(value) else "Not Found\n")

    # ===== DELETE =====
    delete_value = 3
    print(f"Deleting {delete_value}...")
    cdll.delete(delete_value)

    print("After Deletion (Forward):")
    cdll.traverse_forward()

    print("After Deletion (Backward):")
    cdll.traverse_backward()
    print()

    # ===== FINAL DISPLAY =====
    print("Final List (using __str__):")
    print(cdll)


# Entry point
if __name__ == "__main__":
    main()
