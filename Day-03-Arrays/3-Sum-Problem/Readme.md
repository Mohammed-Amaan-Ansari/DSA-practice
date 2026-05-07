# 15. 3Sum

## Problem
Find all unique triplets in the array which gives the sum of zero.

## Example
Input:
nums = [-1,0,1,2,-1,-4]

Output:
[[-1,-1,2],[-1,0,1]]

## Approach
1. Sort the array.
2. Fix one element.
3. Use two pointers for remaining elements.
4. Skip duplicates.

## Complexity
- Time: O(n²)
- Space: O(1)