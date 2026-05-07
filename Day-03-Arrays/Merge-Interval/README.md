# 56. Merge Intervals

## Problem
Merge all overlapping intervals.

## Example
Input:
[[1,3],[2,6],[8,10],[15,18]]

Output:
[[1,6],[8,10],[15,18]]

## Approach
1. Sort intervals.
2. Compare current interval with previous.
3. Merge if overlapping.

## Complexity
- Time: O(n log n)
- Space: O(n)