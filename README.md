# 📘 Linked List Implementations in Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Complete-success)
![Use](https://img.shields.io/badge/Use-Educational-orange)


## 📌 Project Overview

This repository provides **comprehensive implementations of the four fundamental linked list variants** in Python:

1. **Singly Linked List (SLL)**
2. **Circular Singly Linked List (CSLL)**
3. **Doubly Linked List (DLL)**
4. **Circular Doubly Linked List (CDLL)**

Each implementation demonstrates how dynamic data structures use **nodes and pointers (references)** to efficiently manage data without contiguous memory allocation.


## 🎯 Learning Objectives

By exploring this project, users will be able to:

* Understand the **structure and behavior** of linked list variants
* Differentiate between:

  * Linear vs Circular structures
  * Singly vs Doubly linking
* Implement core operations:

  * Insertion
  * Deletion
  * Traversal
  * Searching
* Analyze **time complexity and trade-offs** of each structure

## ⚙️ Core Features

All implementations include:

* Insert at front
* Insert at end
* Delete a node
* Search for a value
* Traverse the list
* String representation (`__str__`)

Additional capabilities:

* Bidirectional traversal (DLL, CDLL)
* Circular traversal handling (CSLL, CDLL)


## 🧱 Linked List Variants

### 1️⃣ Singly Linked List (SLL)

* Each node points to the next node
* The last node points to `None`

```
Head -> A -> B -> C -> None
```

✔ Simple and memory-efficient
❌ No backward traversal


### 2️⃣ Circular Singly Linked List (CSLL)

* The last node points back to the head

```
Head -> A -> B -> C
  ↑                 ↓
  └─────────────────┘
```

✔ Eliminates `None` references
✔ Efficient cyclic traversal
❌ Still single-directional


### 3️⃣ Doubly Linked List (DLL)

* Each node has both `next` and `prev` references

```
None <- A <-> B <-> C -> None
```

✔ Supports forward and backward traversal
✔ Easier node deletion
❌ Higher memory usage


### 4️⃣ Circular Doubly Linked List (CDLL)

* Fully circular in both directions

```
A <-> B <-> C
↑           ↓
└───────────┘
```

✔ Bidirectional and circular traversal
✔ No `None` pointers
✔ Most flexible structure


## 🧩 Node Structure

### Singly / Circular Singly

```
+---------+---------+
|  DATA   |  NEXT   |
+---------+---------+
```

### Doubly / Circular Doubly

```
+---------+---------+---------+
|  DATA   |  NEXT   |  PREV   |
+---------+---------+---------+
```


## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/linked-list-python.git
cd linked-list-python
```

### 2. Run Any Implementation

```bash
python singly_linked_list.py
python circular_singly_linked_list.py
python doubly_linked_list.py
python circular_doubly_linked_list.py
```


## 📊 Time Complexity Analysis

| Operation      | SLL  | CSLL | DLL  | CDLL |
| -------------- | ---- | ---- | ---- | ---- |
| Insert (Front) | O(1) | O(1) | O(1) | O(1) |
| Insert (End)   | O(n) | O(n) | O(n) | O(n) |
| Delete         | O(n) | O(n) | O(n) | O(n) |
| Search         | O(n) | O(n) | O(n) | O(n) |
| Traverse       | O(n) | O(n) | O(n) | O(n) |


## 🔍 Key Differences Summary

| Feature             | SLL | CSLL | DLL | CDLL |
| ------------------- | --- | ---- | --- | ---- |
| Direction           | One | One  | Two | Two  |
| Circular            | No  | Yes  | No  | Yes  |
| Uses `prev` pointer | No  | No   | Yes | Yes  |
| Last points to head | No  | Yes  | No  | Yes  |


## ⚠️ Edge Cases Handled

The implementations account for:

* Empty list operations
* Single-node lists
* Deleting the head node
* Deleting the last node
* Circular traversal termination (avoiding infinite loops)


## 🧪 Educational Applications

This repository is ideal for:

* Data Structures and Algorithms courses
* Laboratory and programming activities
* Concept visualization and comparison
* Self-paced learning and review


## 👨‍💻 Author

**Jun Y. Ercia**
Faculty, Computer Science / Computer Engineering


## 📄 License

This project is intended for **educational use only**.


## ⭐ Contributions

Contributions are welcome. You may:

* Fork the repository
* Enhance existing implementations
* Add new operations (e.g., reverse, sort)
* Integrate visualization or GUI


## 🚀 Future Enhancements

* Insert at specific position
* Reverse linked list
* Sorting algorithms
* Interactive (menu-driven) interface
* Visualization tools (Tkinter / Web-based)

---


