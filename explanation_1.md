Problem 1: LRU Cache

For the LRU problem, a queue is used to store information about how often an element is accessed. Least recently used element is at the head of the queue. When the cache is full, the element at the head of the queue is removed.

Time complexity: all operations are O(1)
    * get operation is O(1) because it is returning value at a given key.
    * set operations is also O(1) because we are adding value by key.
Space complexity: is O(n), where n is size of bucket size. And, O(m) for the queue, where m is queue size. In total O(n+m), which is linear.
