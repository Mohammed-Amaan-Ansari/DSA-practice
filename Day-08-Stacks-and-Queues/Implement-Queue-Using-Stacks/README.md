# Implement Queue using Stacks

## Approach
Use two stacks:
- input_stack → for push
- output_stack → for pop/peek

Transfer elements only when output stack is empty.

## Time Complexity
- push: O(1)
- pop: amortized O(1)
- peek: amortized O(1)

## Space Complexity
O(n)