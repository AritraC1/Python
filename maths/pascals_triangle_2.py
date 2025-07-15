# Pascal Triangle 2: Print the nth row of the pascal traingle

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

def get_row(r: int) -> List[int]:
    if(rowIndex == 0):
        return [1]
    
    ans = 1
    row = [1]

    for i in range (1, r+1):
        ans = ans * (r-i+1)
        ans = ans//i
        row.append(ans)
    
    return row

rowIndex = int(input("Enter the row number: "))
print(get_row(rowIndex))