class Node:
    """
    Represents a single node in a singly linked list.
    """
    def __init__(self, data):
        self.data = data          # Value stored in the node
        self.next = None          # Pointer to the next node


class SinglyLinkedList:
    """
    Implementation of a Singly Linked List.
    Supports basic operations such as insertion, deletion,
    traversal, and searching.
    """
    def __init__(self):
        self.head = None          # Initially, the list is empty

    def is_empty(self):
        """Returns True if the list is empty."""
        return self.head is None

    def search(self, data):
        """
        Searches for a value in the list.
        Returns True if found, otherwise False.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def traverse(self):
        """
        Displays all elements in the list.
        """
        if self.is_empty():
            print("List is empty.")
            return

        current = self.head
        result = "Head -> "

        while current:
            result += f"{current.data} -> "
            current = current.next

        result += "None"
        print(result)

    def insert_at_front(self, data):
        """
        Inserts a node at the beginning of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
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
        while current.next:
            current = current.next

        current.next = new_node

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

        while current:
            if current.data == data:
                if previous is None:
                    # Deleting the head node
                    self.head = current.next
                else:
                    # Deleting a middle or last node
                    previous.next = current.next

                print(f"{data} deleted successfully.")
                return True

            previous = current
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

        return " -> ".join(nodes) + " -> None"


# ================= MAIN PROGRAM =================
def main():
    """
    Demonstrates Singly Linked List operations.
    """

    linked_list = SinglyLinkedList()

    print("=== SINGLY LINKED LIST DEMO ===\n")

    # ===== INSERTION =====
    print("Inserting elements at the end: 1, 2, 3")
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)

    print("Current List:")
    linked_list.traverse()
    print()

    # ===== INSERT AT FRONT =====
    print("Inserting 0 at the front")
    linked_list.insert_at_front(0)

    print("Updated List:")
    linked_list.traverse()
    print()

    # ===== SEARCH =====
    search_value = 2
    print(f"Searching for {search_value}...")
    if linked_list.search(search_value):
        print(f"{search_value} found in the list.\n")
    else:
        print(f"{search_value} not found in the list.\n")

    # ===== DELETE =====
    delete_value = 3
    print(f"Deleting {delete_value}...")
    linked_list.delete(delete_value)

    print("List after deletion:")
    linked_list.traverse()
    print()

    # ===== FINAL DISPLAY =====
    print("Final List (using __str__):")
    print(linked_list)


# Entry point of the program
if __name__ == "__main__":
    main()
