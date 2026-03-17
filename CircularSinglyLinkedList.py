class Node:
    """
    Represents a node in a Circular Singly Linked List.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    """
    Implementation of a Circular Singly Linked List (CSLL).

    In this structure, the last node points back to the head node,
    forming a circular connection.
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

    def traverse(self):
        """
        Displays all elements in the circular list.
        """
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        result = "Head -> "

        while True:
            result += f"{current.data} -> "
            current = current.next

            if current == self.head:
                break

        result += "(back to Head)"
        print(result)

    def insert_at_front(self, data):
        """
        Inserts a node at the beginning of the circular list.
        """
        new_node = Node(data)

        if self.is_empty():
            # First node points to itself
            self.head = new_node
            new_node.next = self.head
            return

        # Find the last node (tail)
        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a node at the end of the circular list.
        """
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        # Traverse to last node
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def delete(self, data):
        """
        Deletes the first occurrence of the given value.
        Returns True if successful, otherwise False.
        """
        if self.is_empty():
            print("Error: List is empty.")
            return False

        current = self.head
        previous = None

        while True:
            if current.data == data:
                # Case 1: Only one node
                if current == self.head and current.next == self.head:
                    self.head = None

                # Case 2: Deleting head node
                elif current == self.head:
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next

                    self.head = current.next
                    tail.next = self.head

                # Case 3: Deleting middle or last node
                else:
                    previous.next = current.next

                print(f"{data} deleted successfully.")
                return True

            previous = current
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

        return " -> ".join(nodes) + " -> (back to Head)"


# ================= MAIN PROGRAM =================
def main():
    """
    Demonstrates Circular Singly Linked List operations.
    """

    csll = CircularSinglyLinkedList()

    print("=== CIRCULAR SINGLY LINKED LIST DEMO ===\n")

    # ===== INSERTION =====
    print("Inserting elements at the end: 1, 2, 3")
    csll.insert_at_end(1)
    csll.insert_at_end(2)
    csll.insert_at_end(3)

    print("Current List:")
    csll.traverse()
    print()

    # ===== INSERT AT FRONT =====
    print("Inserting 0 at the front")
    csll.insert_at_front(0)

    print("Updated List:")
    csll.traverse()
    print()

    # ===== SEARCH =====
    value = 2
    print(f"Searching for {value}...")
    print("Found\n" if csll.search(value) else "Not Found\n")

    # ===== DELETE =====
    delete_value = 3
    print(f"Deleting {delete_value}...")
    csll.delete(delete_value)

    print("List after deletion:")
    csll.traverse()
    print()

    # ===== FINAL DISPLAY =====
    print("Final List (using __str__):")
    print(csll)


# Entry point
if __name__ == "__main__":
    main()
