num = int(input("Enter a number to check whether it is an Armstrong number: "))
if num < 0:
    print("Armstrong numbers are defined only for non-negative integers.")
else:
    temp = num
    digits = len(str(num))
    sum_of_powers = 0
    while temp > 0:
        rem = temp % 10
        sum_of_powers += rem ** digits
        temp //= 10
    if num == sum_of_powers:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
