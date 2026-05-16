# Approach

Compare middle with right.

If nums[mid] > nums[right]:
minimum lies in right half.

Else:
minimum lies in left half.

Time: O(log n)
Space: O(1)

Pattern: Binary Search on Rotated Array