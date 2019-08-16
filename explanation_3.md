Problem 3: huffman coding
============================

A BST is used to implement huffman coding.

Time complexity
---------------
The time complexity of building the tree is O(nlogn) because the insertions and deletions are done in log(n), which are performed n time. 

There is a helper function for sorting, which is built-in sort algorithm, but that is also O(nlogn) because it is a merge sort.

Space complexity 
---------------

Encoding:
* freq is dictionary: grows linearly with the input size.
* a stack is sued to store nodes, which is also linear with the input size.
* a binary search tree is used, which is linear with the input size
The overall space complexity to implement the encoding function is O(n).

Decoding:
* O(n) for the array decoded_data that stores 0 or 1 depending on the traverse on the tree.
