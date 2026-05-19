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

@dataclass(frozen=True)
class MinHeap:
    data: list[Node] = field(default_factory=list)

def swap(data: list[Node], i: int, j: int) -> list[Node]:
    return [
        data[j] if k == i else
        data[i] if k == j else
        data[k]
        for k in range(len(data))
    ]

def heapify_up(heap: MinHeap, index: int) -> MinHeap:
    if index <= 0:
        return heap

    parent = (index - 1) // 2

    if heap.data[index] < heap.data[parent]:
        new_data = swap(heap.data, index, parent)
        return heapify_up(MinHeap(new_data), parent)

    return heap

def insert(heap: MinHeap, element: Node) -> MinHeap:
    new_data = heap.data + [element]
    new_heap = MinHeap(new_data)
    return heapify_up(new_heap, len(new_data) - 1)

def heapify_down(heap: MinHeap, index: int) -> MinHeap:
    data = heap.data
    size = len(data)

    left = 2 * index + 1
    right = 2 * index + 2
    smallest = index

    if left < size and data[left] < data[smallest]:
        smallest = left

    if right < size and data[right] < data[smallest]:
        smallest = right

    if smallest != index:
        new_data = swap(data, index, smallest)
        return heapify_down(MinHeap(new_data), smallest)

    return heap


def extract_min(heap: MinHeap) -> tuple[MinHeap, Node]:
    if len(heap.data) == 0:
        raise IndexError
    if len(heap.data) == 1:
        return MinHeap([]), heap.data[0]

    min_node = heap.data[0]
    last_node = heap.data[-1]

    new_data = [last_node] + heap.data[1:-1]
    new_heap = heapify_down(MinHeap(new_data), 0)

    return new_heap, min_node

        
def count_frequency(s: str)-> dict[str,int]:
    frequency = {}
    for char in s:
        frequency = {**frequency, char: frequency.get(char, 0) + 1}
    return frequency

def create_priority_queue(frequency: dict[str, int]) -> MinHeap:
    heap = MinHeap([])
    for char, freq in frequency.items():
        node = Node(freq, char)
        heap = insert(heap, node)
    return heap


def build_tree(priority_queue: MinHeap) -> Node | None:
    if len(priority_queue.data) == 0:
        return None

    if len(priority_queue.data) == 1:
        return priority_queue.data[0]

    heap1, left = extract_min(priority_queue)
    heap2, right = extract_min(heap1)

    combined = Node(
        left.freq + right.freq,
        left.char + right.char,
        left,
        right
    )

    new_heap = insert(heap2, combined)
    return build_tree(new_heap)


def build_tree_from_queue(priority_queue: MinHeap) -> Node | None:
    return build_tree(priority_queue)


def generate_codes(node: Node | None, prefix="", code: dict | None =None)-> dict:
    if code is None:
        code = {}

    if node is None:
        return code

    if node.left is None and node.right is None:
        return {**code, node.char: prefix if prefix != "" else "0"}

    left_codes = generate_codes(node.left, prefix + "0", code)
    right_codes = generate_codes(node.right, prefix + "1", left_codes)

    return right_codes

def encode(s: str, codes: dict)-> str:
    return "".join(codes[char] for char in s)


def decode(encoded_string: str, root: Node):
    if root is None:
        return ""

    if root.left is None and root.right is None:
        return root.char * len(encoded_string)

    decoded = ""
    current = root

    for bit in encoded_string:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.left is None and current.right is None:
            decoded += current.char
            current = root

    return decoded

def huffman_encoding(s:str):
    #Do Not Change this function
    frequency = count_frequency(s)
    pq = create_priority_queue(frequency)
    root = build_tree(pq)
    codes = generate_codes(root)
    encoded_string = encode(s, codes)
    decoded_string = decode(encoded_string,root)
    return encoded_string, decoded_string, codes


