# Program to check whether a number is a palindrome
num = int(input("Enter a number to check whether it is a palindrome: "))
temp = num
reversed_num = 0
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if num == reversed_num:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")
