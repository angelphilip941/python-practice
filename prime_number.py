num = int(input("Enter a number to check whether it is prime or not: "))

if num <= 1:
    print("Number is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is a prime number")
