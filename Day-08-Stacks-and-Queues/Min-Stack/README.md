# Min Stack

## Approach
Use two stacks:
- stack → actual values
- min_stack → current minimum values

## Key Idea
Whenever new value <= current min:
push it into min_stack.

## Time Complexity
All operations → O(1)

## Space Complexity
O(n)