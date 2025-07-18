# Recursion in Python
Recursion is a programming technique where a function calls itself to solve smaller instances of a problem until it reaches a base case, in other words recursion is a function that calls intself with a exit base case.

## Key Components of Recursion
1. **Base Case:** The condition under which the function stops calling itself.

2. **Recursive Case:** The part where the function calls itself with a smaller or simpler input.

## Flow Diagram of a Recursion
![Flow Diagram of Recursion](assets/FD_Recursion.png)

## Examples with Flow Diagram

### Example 1: Print numbers
```python []
def print_numbers(lower, upper):
    # Base case
    if lower > upper:
        return # when true, exit code
    
    print(lower)
    print_numbers(lower+1, upper)


print_numbers(1, 5) # output: 1 2 3 4 5
```
![]()

### Example 2: Print Pattern
```python []

```
![]()

### Example 3: Factorial
```python []

```
![]()
## Common Pitfalls
- **Missing Base Case:** Leads to infinite recursion → RecursionError.
- **Improper Recursive Step:** Might not reach the base case.

## Recursion vs Iteration
| Feature      | Recursion                        | Iteration               |
| ------------ | -------------------------------- | ----------------------- |
| Structure    | Function calls itself            | Uses loops (for, while) |
| Memory usage | More (stack frames)              | Less                    |
| Speed        | Often slower                     | Often faster            |
| Readability  | More elegant (for some problems) | Can be more efficient   |

## When to Use Recursion?
- Tree traversals (e.g., binary trees)
- Divide and conquer algorithms (e.g., mergesort, quicksort)
- Problems with naturally recursive structure (e.g., Fibonacci numbers, permutations)