from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Node:
    freq: int
    char: str
    left: Node | None = None
    right: Node | None  = None

    def __str__(self):
        return f"Node: {self.char}, Freq: {self.freq}"

from dataclasses import dataclass, field

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    if index == 0:
        return heap  # Base case: reached the root of the heap
    parent_index = (index - 1) // 2
    heap_data = heap.data
    if heap_data[index] < heap_data[parent_index]:
        new_heap_data = heap_data[:]
        new_heap_data[index], new_heap_data[parent_index] = new_heap_data[parent_index], new_heap_data[index]
        return heapify_up(MinHeap(new_heap_data), parent_index)
    else:
        return heap  # No swap needed, return the heap as is

def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_heap_data = heap.data[:] + [element]
    last_index = len(new_heap_data) - 1
    new_heap = heapify_up(MinHeap(new_heap_data), last_index)
    return new_heap

def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    heap_data = heap.data
    current_size = len(heap_data)
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < current_size and heap_data[left] < heap_data[smallest]:
        smallest = left

    if right < current_size and heap_data[right] < heap_data[smallest]:
        smallest = right

    if smallest != index:
        new_heap_data = heap_data[:]
        new_heap_data[index], new_heap_data[smallest] = new_heap_data[smallest], new_heap_data[index]
        return heapify_down(MinHeap(new_heap_data), smallest)
    else:
        return heap  # No swap needed, return the heap as is

def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    if not heap.data:
        raise ValueError("Heap is empty")

    min_element = heap.data[0]
    new_heap_data = heap.data[:]
    last_index = len(new_heap_data) - 1
    new_heap_data[0] = new_heap_data[last_index]
    new_heap_data = new_heap_data[:last_index]
    new_heap = heapify_down(MinHeap(new_heap_data), 0)
    return new_heap, min_element


        
def count_frequency(s: str)-> dict[str,int]:
    #Generate a dictionary that will be key: value pairs of
    # char:frequency 
    #return the dictionary
    frequency: dict[str, int] = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency


def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    """
    Accepts a frequency dictionary where the keys are characters (as strings)
    and the values are their corresponding frequencies (as integers).
    Returns a priority queue (MinHeap) filled with nodes where each node represents a character and its frequency.

    Parameters:
    - frequency: dict[str, int]: A dictionary mapping characters to their frequencies.

    Returns:
    - MinHeap: A priority queue where each element is a Node containing a frequency and a character,
               and the elements are ordered by frequency in a min-heap structure.
    """
    
    # Initialize an empty MinHeap. This will be used to store the nodes created from the frequency dictionary.

    
    # Iterate over each item in the frequency dictionary.

        # Create a new Node for each character and its frequency.
        # The Node is typically defined with at least two properties: frequency and character.
        # Here, frequency is used to determine the order in the heap, and character is the value the node represents.

        
        # Insert the newly created node into the priority queue.
        # The 'insert' function is part of the MinHeap's interface, which adds a new element while maintaining
        # the heap property. In a min-heap, the parent node's frequency is always less than or equal to its children's frequencies.

    
    # After all nodes are inserted into the priority queue, return the completed min-heap.
    # This heap is now ready to be used for further operations, such as building a Huffman tree.
    return priority_queue



def build_tree_from_queue(priority_queue: MinHeap) -> Node:
    """
    Takes a priority queue (min-heap) and constructs the Huffman tree.
    This priority queue should contain all nodes with their frequencies,
    where each node might represent a character or a previously merged subtree.
    """
    def build_recursive(queue):
        # Base case: only one node left in the queue
            # Extract and return the only node left, which is the root of the Huffman tree.
            # extract_min returns a tuple, second element is the node

        # Extract the two nodes with the lowest frequency from the priority queue
        # Remove and get the node with the smallest frequency as left
        # Remove and get the node with the next smallest frequency as right

        # Create a new node that combines these two nodes.
        # The new node's frequency is the sum of the two extracted nodes' frequencies.
        # Choose the character with the lower lexicographical order for the new node for consistent handling, if needed.


        # Enqueue the newly created merged node back into the priority queue

        # Recursively call to continue merging the nodes until only one remains


    # Initiate the recursive tree building and return the root of the Huffman tree
    return build_recursive(priority_queue)



def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}  

    #Traverse the tree to generate a huffman encoding
    # the huffman encoding will be a dictionary char:encoding pairs
    #if node is Node return code
    #if node has a char, then code[node.char] = prefix
    #recursively calls generate_codes on the left, with prefix + "0" and code
    #recursively calls generate_codes on the right, with prefix + "1" and code
    #returns the code dictionary


def encode(s: str, codes: dict)-> str:
    #This is given to you
    return ''.join(codes[char] for char in s)

def decode(encoded_string: str, root: Node):
    """
    Decode an encoded string using the provided Huffman tree in a purely functional manner,
    now using an index to track position in the string.
    """
    def decode_recursive(encoded: str, node: Node, root: Node, index: int) -> str:

        # If index is out of bounds, return the char you are on
        # Check if the current node is a leaf (i.e., no children)
            # If at a leaf node, decode this character and restart from the root
            # Continue decoding from the current index since the current character has been processed

        # Determine the next node based on the character at the current index

        
        # Continue decoding with the next node, incrementing the index


    # Initialize the recursive function by passing the encoded string, the root node as the starting node,
    # the root node as a reference to restart, and 0 as the starting index
    return decode_recursive(encoded_string, root, root, 0)




def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree_from_queue(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes


#print(huffman_encoding("hello"))
#print(huffman_encoding("google"))
#print(huffman_encoding("potato"))
