# Approach

Treat matrix as sorted 1D array.

Convert:
row = mid // cols
col = mid % cols

Time: O(log(m*n))
Space: O(1)

Pattern: Binary Search on Matrix