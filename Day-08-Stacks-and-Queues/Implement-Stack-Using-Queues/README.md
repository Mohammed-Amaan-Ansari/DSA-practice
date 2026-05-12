# Implement Stack using Queues

## Approach
Use one queue.

After pushing:
Rotate all previous elements behind the new one.

## Time Complexity
- push: O(n)
- pop: O(1)

## Space Complexity
O(n)