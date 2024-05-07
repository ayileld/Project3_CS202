# Project 3: Huffman Encoding

## Overview
Project3 is an implementation of Huffman Encoding, a widely used method for data compression. This project includes a detailed exploration of the Huffman encoding process, from frequency counting to tree construction and binary encoding/decoding. Special emphasis is placed on the `Node` and `MinHeap` classes provided, which are pivotal in constructing the Huffman tree and managing the priority queue, respectively.

## Features
- **Frequency Counting:** Analyzes the frequency of each character in the input string.
- **Priority Queue:** Utilizes a MinHeap to maintain the characters sorted by their frequencies.
- **Huffman Tree Construction:** Builds a Huffman tree based on character frequencies.
- **Encoding and Decoding:** Generates binary codes for characters and decodes them back to the original string.
- `https://asecuritysite.com/calculators/huff`
- You can use the above link to generate examples

## Tasks
Complete the implementation of the following functions:

1. **`create_priority_queue(frequency: dict[str, int]) -> MinHeap`**:
   - Complete the implementation to accept a frequency dictionary, create nodes for each character and its frequency, and insert them into a priority queue (MinHeap).

   - With the frequency dictionary in hand, create a priority queue that organizes the characters based on their frequencies. This step is crucial for building the Huffman tree and is accomplished by invoking `create_priority_queue`, which returns a `MinHeap` filled with `Node` objects for each character.

2. **`build_tree_from_queue(priority_queue: MinHeap) -> Node`**:
   - Complete the function to construct the Huffman tree from the provided priority queue.

   - Construct the Huffman tree from the priority queue by calling `build_tree_from_queue`. This function iteratively combines the nodes with the least frequencies into new nodes until a single node remains, representing the root of the Huffman tree.

3. **`generate_codes(node: Node | None, prefix="", code: dict | None = None) -> dict`**:
   - Implement the function to traverse the Huffman tree and generate Huffman codes for each character.

   - Generate the Huffman codes for each character by traversing the newly constructed Huffman tree. The `generate_codes` function accomplishes this, returning a dictionary where each character is mapped to its corresponding binary code.

4. **`decode(encoded_string: str, root: Node)`**:
   - Implement this function to decode an encoded string using the provided Huffman tree, utilizing a purely functional manner and tracking position in the string using an index.

   - Decode the binary string back into its original text form to verify the accuracy of the Huffman encoding process. This is achieved through the `decode` function, which utilizes the Huffman tree to interpret the binary sequence back into text.

## Resources Provided
- **Data Structures**: `Node` and `MinHeap` classes to help with the construction of the Huffman tree and priority queue.
- **Utility Functions**: `heapify_up`, `heapify_down`, `insert`, and `extract_min` for managing the MinHeap operations.
- **Encoding Function**: `encode(s: str, codes: dict) -> str`, which is provided complete and should be used as is.

## Testing Requirements
- **Test File**: You must pass all tests in `test_p3.py`.
- **Additional Tests**: Write your own tests in `test_student.py`. There are no set expectations on your tests; they are primarily to ensure your code is prepared for potential test cases that might be used for evaluation.

## Instructions
1. **Understand Huffman Coding**: Before you start, make sure you understand how Huffman coding works.
2. **Complete the Functions**: Use the provided data structures and helper functions to complete the aforementioned functions.
3. **Test Thoroughly**: After completing the functions, use `test_p3.py` to test the functionality. Additionally, write your own tests in `test_student.py` to catch any edge cases or potential bugs.
4. **Ensure Functionality**: Your final submission should pass all tests and correctly implement the process of Huffman encoding and decoding.

Feel free to refer to online resources for understanding Huffman coding but ensure all code submissions are your own work.

## Submission
- Complete all required functions.
- Ensure all tests in `test_p3.py` pass.
- Write and pass your tests in `test_student.py`.
- Submit your project by the deadline provided via github.

