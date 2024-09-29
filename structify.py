def LinearSearchBool(any_list, target):
    """ 
    Perform a linear search to check if the target exists in the list.
    
    Args:
        any_list (list): The list to search through.
        target: The item to search for.
        
    Returns:
        bool: True if the target is found, False otherwise.
    """
    return target in any_list


def LinearSearchIndex(any_list, target):
    """ 
    Perform a linear search to find the index of the target in the list.
    
    Args:
        any_list (list): The list to search through.
        target: The item to search for.
        
    Returns:
        int or bool: The index of the target if found, False otherwise.
    """
    for i, item in enumerate(any_list):
        if item == target:
            return i
    return False


def BinarySearch(any_list, target):
    """ 
    Perform a binary search to check if the target exists in a sorted list.
    
    Args:
        any_list (list): The sorted list to search through.
        target: The item to search for.
        
    Returns:
        bool: True if the target is found, False otherwise.
    """
    first, last = 0, len(any_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if any_list[mid] == target:
            return True
        elif any_list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return False


def BinarySearchIndex(any_list, target):
    """ 
    Perform a binary search to find the index of the target in a sorted list.
    
    Args:
        any_list (list): The sorted list to search through.
        target: The item to search for.
        
    Returns:
        int or bool: The index of the target if found, False otherwise.
    """
    first, last = 0, len(any_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if any_list[mid] == target:
            return mid
        elif any_list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return False


def RecursiveBinarySearch(any_list, target):
    """ 
    Perform a recursive binary search to check if the target exists in a sorted list.
    
    Args:
        any_list (list): The sorted list to search through.
        target: The item to search for.
        
    Returns:
        bool: True if the target is found, False otherwise.
    """
    if not any_list:
        return False
    
    mid = len(any_list) // 2
    if any_list[mid] == target:
        return True
    elif any_list[mid] < target:
        return RecursiveBinarySearch(any_list[mid + 1:], target)
    else:
        return RecursiveBinarySearch(any_list[:mid], target)


def RecursiveBinarySearchIndex(any_list, target, offset=0):
    """ 
    Perform a recursive binary search to find the index of the target in a sorted list.
    
    Args:
        any_list (list): The sorted list to search through.
        target: The item to search for.
        offset (int): The current offset in the original list.
        
    Returns:
        int or bool: The index of the target if found, False otherwise.
    """
    if not any_list:
        return False
    
    mid = len(any_list) // 2
    if any_list[mid] == target:
        return mid + offset
    elif any_list[mid] < target:
        return RecursiveBinarySearchIndex(any_list[mid + 1:], target, offset + mid + 1)
    else:
        return RecursiveBinarySearchIndex(any_list[:mid], target, offset)


def split(any_list):
    """ 
    Split the list into two halves.
    
    Args:
        any_list (list): The list to be split.
        
    Returns:
        tuple: Two halves of the original list.
    """
    mid = len(any_list) // 2
    return any_list[:mid], any_list[mid:]


def merge(list1, list2):
    """ 
    Merge two sorted lists into a single sorted list.
    
    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.
        
    Returns:
        list: The merged sorted list.
    """
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list
def MergeSort(any_list, SortType='ascending'):
    """ 
    Perform merge sort on the given list.
    
    Args:
        any_list (list): The list to be sorted.
        SortType (str): Type of sorting ('ascending' or 'descending').
        
    Returns:
        list: The sorted list.
    """
    if len(any_list) <= 1:
        return any_list    
    left_half, right_half = split(any_list)
    left = MergeSort(left_half, SortType)
    right = MergeSort(right_half, SortType)
    return merge(left, right)


class LinkedList:
    """ A class for singly and doubly linked lists. """
    
    class Node:
        """ A node in a linked list. """
        def __init__(self, value=0, prev=None, next=None):
            self.prev = prev
            self.value = value
            self.next = next
        
    class SinglyLinkedList:
        """ A singly linked list implementation. """
        def __init__(self):
            self.head = None

        def append(self, value):
            """ Append a value to the end of the list. """
            new_node = LinkedList.Node(value)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

        def display(self):
            """ Print the values in the list. """
            current = self.head
            while current:
                print(current.value, end="->" if current.next else "")
                current = current.next

        def size(self):
            """ Return the number of elements in the list. """
            length = 0
            current = self.head
            while current:
                current = current.next
                length += 1
            return length    

        def searchfor(self, target):
            """ Search for a target value in the list. """
            if self.size() == 0:
                return "List is empty"
            current = self.head
            while current:
                if current.value == target:
                    return f"{current.value} found at instance {current}"
                current = current.next

        def insertAt(self, data, index):
            """ Insert a value at a specific index in the list. """
            new_node = LinkedList.Node(data)
            if index > self.size() or index < 0:
                raise IndexError("Index out of bounds")

            if index == 0:
                new_node.next = self.head
                if self.head:
                    self.head.prev = new_node
                self.head = new_node
                return

            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
            if new_node.next:
                new_node.next.prev = new_node

        def removeValue(self, target):
            """ Remove the first occurrence of a value from the list. """
            current = self.head
            previous = None
            position = 0

            while current:
                if current.value == target:
                    print("Value found at index", position)
                    if previous is None:
                        self.head = current.next
                        if current.next:
                            current.next.prev = None
                    else:
                        previous.next = current.next
                        if current.next:
                            current.next.prev = previous
                    return  
                previous = current
                current = current.next
                position += 1

    class DoublyLinkedList:
        """ A doubly linked list implementation. """
        def __init__(self):
            self.head = None

        def append(self, value):
            """ Append a value to the end of the list. """
            new_node = LinkedList.Node(value)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
                new_node.prev = current

        def displayforward(self):
            """ Print the values from head to tail. """
            current = self.head
            while current:
                print(current.value, end="->" if current.next else "")
                current = current.next

        def displaybackward(self):
            """ Print the values from tail to head. """
            current = self.head
            while current and current.next:
                current = current.next
            while current:
                print(current.value, end="<-" if current.prev else "")
                current = current.prev

        def searchfor(self, target):
            """ Search for a target value in the list. """
            if self.size() == 0:
                return "List is empty"
            current = self.head
            while current:
                if current.value == target:
                    return f"{current.value} found at instance {current}"
                current = current.next

        def size(self):
            """ Return the number of elements in the list. """
            length = 0
            current = self.head
            while current:
                current = current.next
                length += 1
            return length 

        def insertAt(self, data, index):
            """ Insert a value at a specific index in the list. """
            new_node = LinkedList.Node(data)
            if index > self.size() or index < 0:
                raise IndexError("Index out of bounds")

            if index == 0:
                new_node.next = self.head
                if self.head:
                    self.head.prev = new_node
                self.head = new_node
                return

            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next = new_node
            if new_node.next:
                new_node.next.prev = new_node

        def removeValue(self, target):
            """ Remove the first occurrence of a value from the list. """
            current = self.head
            previous = None
            position = 0

            while current:
                if current.value == target:
                    print("Value found at index", position)
                    if previous is None:
                        self.head = current.next
                        if current.next:
                            current.next.prev = None
                    else:
                        previous.next = current.next
                        if current.next:
                            current.next.prev = previous
                    return  
                previous = current
                current = current.next
                position += 1


def QuickSort(any_list):
    """ 
    Perform quicksort on the given list.
    
    Args:
        any_list (list): The list to be sorted.
        
    Returns:
        list: The sorted list.
    """
    if len(any_list) < 1:
        return any_list
    pivot = any_list[len(any_list) // 2]
    left = [x for x in any_list if x < pivot]
    middle = [x for x in any_list if x == pivot]
    right = [x for x in any_list if x > pivot]

    return QuickSort(left) + middle + QuickSort(right)


def SelectionSort(any_list):
    """ 
    Perform selection sort on the given list.
    
    Args:
        any_list (list): The list to be sorted.
        
    Returns:
        list: The sorted list.
    """
    for pt_head in range(len(any_list)):
        min_idx = pt_head
        for i in range(pt_head + 1, len(any_list)):
            if any_list[i] < any_list[min_idx]:
                min_idx = i
        any_list[pt_head], any_list[min_idx] = any_list[min_idx], any_list[pt_head]
    return any_list


def SumWithRecursion(any_list):
    """ 
    Calculate the sum of elements in the list using recursion.
    
    Args:
        any_list (list): The list of numbers to sum.
        
    Returns:
        int: The sum of the numbers.
    """
    if len(any_list) == 0:
        return 0
    return any_list[0] + SumWithRecursion(any_list[1:])
class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        print("Adding", value)
        self.items.append(value)

    def dequeue(self):
        if len(self.items) == 0:
            return "Queue is empty"
        i = self.items[0]
        self.items = self.items[1:]
        print("Removing", i)
        return i

    def inQueue(self, val):
        return val in self.items

    def peek(self):
        if not self.isempty():
            return self.items[0]
        return "Empty Queue"

    def size(self):
        return len(self.items)

    def __repr__(self):
        return "Queue %s" % "<-".join([str(s) for s in self.items])


class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex_name):
        # Initialize an empty list for each vertex
        self.graph[vertex_name] = []

    def add_edge(self, from_vertex, to_vertex, edge_cost):
        if from_vertex in self.graph and to_vertex in self.graph:
            # Append a tuple (connected vertex, cost) to the adjacency list
            self.graph[from_vertex].append((to_vertex, edge_cost))
            self.graph[to_vertex].append((from_vertex, edge_cost))  # For undirected graph
        else:
            return "One of the vertices is not in the graph"

    def __repr__(self):
        # Format the adjacency list into a string for representation
        return '\n'.join(f"{vertex}: {edges}" for vertex, edges in self.graph.items())


def bfs(g: Graph, start_vertex):
    visited = set()
    queue = Queue()
    queue.enqueue(start_vertex)
    visited.add(start_vertex)

    while not queue.isempty():
        current_vertex = queue.dequeue()
        
        for neighbour, cost in g.graph[current_vertex]:
            if neighbour not in visited:
                print("Current :", current_vertex, "is connected to", neighbour)
                visited.add(neighbour)
                queue.enqueue(neighbour)


def dfs(g: Graph, start_vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_vertex)
    print("Visiting:", start_vertex)
    
    for neighbour, cost in g.graph[start_vertex]:
        if neighbour not in visited:
            dfs(g, neighbour, visited)


# Example Implementation
# g = Graph()

# # Add cities (vertices)
# g.add_vertex("New York")
# g.add_vertex("Los Angeles")
# g.add_vertex("Chicago")
# g.add_vertex("Houston")
# g.add_vertex("Phoenix")
# g.add_vertex("Philadelphia")
# g.add_vertex("San Antonio")
# g.add_vertex("San Diego")
# g.add_vertex("Dallas")
# g.add_vertex("San Jose")

# # Add edges with costs
# g.add_edge("New York", "Los Angeles", edge_cost=2800)
# g.add_edge("New York", "Chicago", edge_cost=790)
# g.add_edge("Los Angeles", "Houston", edge_cost=1370)
# g.add_edge("Houston", "Chicago", edge_cost=1080)
# g.add_edge("Chicago", "Phoenix", edge_cost=1440)
# g.add_edge("Phoenix", "San Diego", edge_cost=350)
# g.add_edge("San Diego", "Los Angeles", edge_cost=120)
# g.add_edge("San Antonio", "Dallas", edge_cost=275)
# g.add_edge("Dallas", "Houston", edge_cost=240)
# g.add_edge("Philadelphia", "New York", edge_cost=95)
# g.add_edge("San Jose", "San Diego", edge_cost=500)
# g.add_edge("Philadelphia", "Chicago", edge_cost=780)

# print("Graph representation:")
# print(g)

# # Perform BFS and DFS
# print("\nBFS traversal starting from New York:")
# bfs(g, "New York")

# print("\nDFS traversal starting from New York:")
# dfs(g, "New York")
