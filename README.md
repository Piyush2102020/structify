# Structify


**Structify** is a lightweight Python library designed to simplify and enhance the process of working with data structures and algorithms. With a variety of built-in data structures and algorithms, Structify provides an easy-to-use interface for developers and enthusiasts alike.

## Features

- **Rich Data Structures**: Easily create and manipulate linked lists, queues, and graphs.
- **Sorting Algorithms**: Implement popular sorting algorithms such as Merge Sort, Quick Sort, and Selection Sort.
- **Graph Traversal**: Perform depth-first and breadth-first search on graphs.
- **Recursion Utilities**: Utilize recursive functions for problem-solving, such as summing a list of numbers.
- **Simple API**: An intuitive interface makes it easy to integrate into any project.


## Usage

### Example: Creating a Linked List

```python
from structify import LinkedList

# Create a new linked list
linked_list = LinkedList.SinglyLinkedList() #or you can use DoublyLinkedList

# Append values
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

# Display the linked list
linked_list.display()  # Output: 10->20->30
```

### Example: Graph Implementation

```python
from structify import Graph

# Create a new graph
g = Graph()

# Add vertices
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

# Add edges
g.add_edge("A", "B", edge_cost=5)
g.add_edge("A", "C", edge_cost=10)

# Print the graph
print(g)
```

### Sorting Algorithms

```python
from structify import MergeSort, QuickSort, SelectionSort

# Example list
my_list = [5, 2, 9, 1, 5, 6]

# Sorting
sorted_list = MergeSort(my_list)
print(sorted_list)  # Output: [1, 2, 5, 5, 6, 9]
```

## Contributing

Contributions are welcome! If you would like to contribute to Structify, please fork the repository and submit a pull request.


## Contact

For any questions or feedback, please reach out to bhattpiyush03@gmail.com
