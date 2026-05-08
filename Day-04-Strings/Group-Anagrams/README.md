# 💡 Approach

## Idea
Sort each word and use sorted string as hashmap key.

Words with same sorted form are anagrams.

## Time Complexity
O(n * k log k)

n = number of strings
k = max string length

## Space Complexity
O(n)

## Pattern
Hashing + Sorting