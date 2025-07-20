'''
To print - 

*
**
***
****
*****
'''

def print_pattern(n, current=1):
    if current > n:
        return
    print('*' * current)
    print_pattern(n, current + 1)

print_pattern(5)