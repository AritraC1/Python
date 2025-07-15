# Check if a number is Palindrome or not
# An integer is a palindrome when it reads the same forward and backward.
# For example, 121 is a palindrome while 123 is not.

def check_palindrome(num)-> bool:
    if num < 0:
        return False
        
    rev_num = 0
    org_num = num
        
    while org_num != 0:
        rev_num = rev_num * 10 + org_num % 10
        org_num = org_num // 10
        
    return num == rev_num

num = int(input("Enter number = "))
ans = check_palindrome(num)

if(ans):
    print("True")
else:
    print("False")