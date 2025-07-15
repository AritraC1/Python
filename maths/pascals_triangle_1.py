# Pascal Triangle 1: Given row 'r' and column 'c', find the element at that place. Eg. input: r = 5, c = 3 output: 6 

'''
Example of Pascal Triangle

     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1

'''

def ncr(r: int, c: int) -> int:
    result = 1

    for i in range (0, c):
        result = result * (r-i)
        result = result // (i+1)
    
    return result


r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

#In Pascal’s Triangle, the value at row r and column c is C(r-1, c-1) because combinations start counting from 0, but rows and columns start from 1.
print(f"Element at row {r} and column {c} is:", ncr(r-1, c-1)) 