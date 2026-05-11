# Add Two Numbers

## Approach
Traverse both linked lists at the same time, add corresponding digits, and keep track of carry.

## Key Idea
Each node stores one digit in reverse order, so addition works like normal digit-wise addition.

## Time Complexity
O(max(m, n))

## Space Complexity
O(max(m, n))