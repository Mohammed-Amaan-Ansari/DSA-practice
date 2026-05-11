# Intersection of Two Linked Lists

## Approach
Use two pointers. When one pointer reaches the end, move it to the other list head.

## Why it works
Both pointers travel the same total distance, so they meet at the intersection node or both become None.

## Time Complexity
O(m + n)

## Space Complexity
O(1)