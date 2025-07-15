# LC 118. Pascal's Triangle

'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 

Constraints:
1 <= numRows <= 30
'''

from typing import List

'''
# Brute Force

def ncr(r: int, c: int) -> int:
    result = 1

    for i in range (c):
        result = result * (r-i)
        result = result // (i+1)
    
    return result

def generate(numRows: int) -> List[List[int]]:
    ans = []

    for row in range (numRows):
        temp = []

        for col in range (row+1):
            temp.append(ncr(row, col))
        
        ans.append(temp)
    
    return ans
'''

def generate(numRows: int) -> List[List[int]]:
    ans = []
    
    for row in range(numRows):
        temp = [1]  # First element is always 1
        prev = 1

        for col in range(1, row + 1):
            # Use the relation: C(n, k) = C(n, k-1) * (n-k+1) / k
            curr = prev * (row - col + 1) // col
            temp.append(curr)
            prev = curr
            
        ans.append(temp)

    return ans

numRows = int(input("Enter the number of rows: "))
print (generate(numRows))