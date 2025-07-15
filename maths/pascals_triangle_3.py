# Pascal Triangle 3: Print the entire Pascal Triangle

'''
Example of Pascal Triangle:

r=1,      1
r=2,     1 1
r=3,    1 2 1
r=4,   1 3 3 1
r=5,  1 4 6 4 1
r=6, 1 5 10 10 5 1

'''

from typing import List

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

numRows = int(input("Enter the number of rows: "))
print(generate(numRows))