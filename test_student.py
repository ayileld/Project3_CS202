rt unittest

from proj3 import (
    Node,
    MinHeap,
    heapify_up,
    heapify_down,
    insert,
    extract_min,
    count_frequency,
    create_priority_queue,
    build_tree,
    build_tree_from_queue,
    generate_codes,
    encode,
    decode,
    huffman_encoding
)

class TestHuffman(unittest.TestCase):

    def test_count_frequency(self):
        self.assertEqual(
            count_frequency("hello"),
            {"h": 1, "e": 1, "l": 2, "o": 1}
        )

    def test_insert_extract_min(self):
        heap = MinHeap([])

        heap = insert(heap, Node(5, "a"))
        heap = insert(heap, Node(2, "b"))
        heap = insert(heap, Node(8, "c"))

        heap, smallest = extract_min(heap)

        self.assertEqual(smallest.char, "b")
        self.assertEqual(smallest.freq, 2)
        self.assertEqual(len(heap.data), 2)

    def test_encode_decode_simple(self):
        s = "aaabbc"

        freq = count_frequency(s)
        heap = create_priority_queue(freq)
        root = build_tree_from_queue(heap)
        codes = generate_codes(root)

        encoded = encode(s, codes)
        decoded = decode(encoded, root)

        self.assertEqual(decoded, s)

    def test_empty_string(self):
        s = ""

        freq = count_frequency(s)
        heap = create_priority_queue(freq)
        root = build_tree_from_queue(heap)
        codes = generate_codes(root)

        self.assertEqual(encode(s, codes), "")
        self.assertEqual(decode("", root), "")

    def test_single_character(self):
        s = "aaaa"

        freq = count_frequency(s)
        heap = create_priority_queue(freq)
        root = build_tree_from_queue(heap)
        codes = generate_codes(root)

        encoded = encode(s, codes)
        decoded = decode(encoded, root)

        self.assertEqual(codes, {"a": "0"})
        self.assertEqual(encoded, "0000")
        self.assertEqual(decoded, "aaaa")


if __name__ == "__main__":
    unittest.main()
